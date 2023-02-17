#### 性能因素 推荐一个SQL实例独占一个服务器
1. 硬件因素 (CPU 可用内存 热数据 网络 I/O)
2. 服务器系统优化
    ```base
   (centos 内核: /etc/sysctl.conf)
        # 每个端口监听队列的长度 及 连接数
        net.core.somaxconn = 65535 
        net.core.netdev_max_backlog = 65535
        net.ipv4.tcp_max_syn_backlog = 65535
        # TCP连接 回收
        net.ipv4.tcp_fin_timeout = 10
        net.ipv4.tcp_tw_reuse = 1
        net.ipv4.tcp_tw_recycle = 1
        # 网络接收或发送(读/写)缓冲区
        net.core.wmem_default = 87380
        net.core.wmem_max = 16777216
        net.core.rmem_default = 87380
        net.core.rmem_default = 16777216
        # 失效连接
        net.ipv4.tcp_keepalive_time = 120
        net.ipv4.tcp_keepalive_intvl = 30
        net.ipv4.tcp_keepalive_probes = 3
        # 内存
        kernel.shmmax = 4294967295 (4G / 物理内存-1byte)
        vm.swappiness = 0 (swap 交换区)
   (centos 资源: /etc/security/limit.conf)
        末尾添加: 
   '*'-所有用户有效 'soft'-当前系统 'hard'-穷尽可能得最大值 'nofile'-打开文件的最大数目
        * soft nofile 65535
        * hard nofile 65535
   (centos 磁盘策略: /sys/block/devname/queue/scheduler)
   # 查看当前策略命令:
        cat /sys/block/devname/queue/scheduler
        noop anticipatory deadline[cfq] 
        [cfq]  # 完全公平策略 适合桌面 不太适合mysql
        [noop] # 同一类型插入 电梯式 饿死读利于写
        [deadline] # 截止时间 对数据库最好
        [anticipatory] # 适合较多写入较少读 如文件服务器
   改为deadline命令:
   echo deadline > /sys/block/sda/queue/scheduler
   (centos 磁盘文件类型)
        EXT3/4 系统挂载参数 /etc/fstab
        data = writeback | ordered | journal(InnoDB推荐使用 writeback)
        noatime,nodiratime 降低日志占用资源 
   # 完整配置示例:
        /dev/sda1/ext4 noatime,nodiratime,data=writeback 1 1
    ```
3. 数据库引擎    
MyISAM引擎:不支持事务,表级锁.   
InnoDB支持事务,行级锁,ACID ,mysql5.5之后默认使用InnoDB.    
CSV引擎以文本方式存储,列不为空,没有索引.  
Archive引擎:适合日志/数据采集,空间占用小,只支持insert/select,只支持自增key建索引.    
Memory引擎:数据存在内存,表结构在硬盘,所有字段定长varchar(10)=char(10),不支持text/blog大字段  
Federated引擎:访问远程mysql服务器,本地不存数据,只保存表结构和连接远程服务器信息
   ```mysql
   # 查看InnoDB存储方式命令 show variables like ... 查看配置
   # innodb_file_per_table on 独立表空间 off 系统表空间
   show variables like 'innodb_file_per_table';  
   # 修改命令
   set global innodb_file_per_table=on;
   ```
4. 配置参数    
   ```zsh
   # 查看mysql读取配置文件路径优先级
   mysqld --help --verbose | grep -A 1 'Default options' 
   # mysql客户端修改全局配置 set global 参数名=参数值; set @@global.参数名=参数值;
   # 会话参数: set [session] 参数名=参数值; set @@session.参数名=参数值;
   # 内存参数防止过大内存溢出: sort_buffer_size连接排序内存缓冲区大小,join_buffer_size链表缓冲区,read_buffer_size:查询读4K倍数,
   # read_rnd_buffer_size索引缓冲区大小
   # Innodb_buffer_pool_size缓存池大小严重影响性能 = 总内存-(每个线程所需内存*连接数)-系统保留内存
   # 允许最大连接数 通常设置2000以上 max_connections=2000
   ```
5. 基准测试 多次运行对比
   > 系统基本信息脚本 get_test_info.sh
   ```zsh
   #!/bin/bash
   INTERVAL=5 # 收集信息间隔时间
   PREFIX=/home/benchmarks/$INTERVAL-sec-status # 信息保存目录
   RUNFILE=/home/benchmarks/running # 运行标识文件, 删除此文件可停止运行
   echo "1" > $RUNFILE #
   MYSQL=/usr/local/mysql/bin/mysql  #mysql目录
   $MYSQL -e "show global variables" >> mysql-variables #mysql设置信息
   while test -e $RUNFILE; do #循环
       file=$(date +%F_%I)
       sleep=$(date +%s.%N | awk '{print 5 - ($1 % 5)}')
       sleep $sleep
       ts="$(date +"TS %s.%N %F %T")"
       loadavg="$(uptime)" # 系统负载
       echo "$ts $loadavg" >> $PREFIX-${file}-status # 
       $MYSQL -e "show global status" >> $PREFIX-${file}-status & # mysql全局状态信息
       echo "$ts $loadavg" >> $PREFIX-${file}-innodbstatus
       $MYSQL -e "show engine innodb status" >> $PREFIX-${file}-innodbstatus & # innodb 状态
       echo "$ts $loadavg" >> $PREFIX-${file}-processlist
       $MYSQL -e "show full processlist\G" >> $PREFIX-${file}-processlist & # 线程状态
       echo $ts
   done
   echo Exiting because $RUNFILE does not exists
   ```
   > 保存及分析 QPS 结果 analyze.sh
   ```zsh 
   #!/bin/bash
   awk '
      BEGIN {
        printf "#ts date time load QPS";
        fmt=" %.2f";
      }
      /^TS/ {
      ts = substr($2,1,index($2,".")-1);
      load = NF -2;
      diff = ts - prev_ts;
      printf "\n%s %s %s %s",ts,$3,$4,substr($load,1,length($load)-1);
      prev_ts=ts;
      }
      /Queries/{
      printf fmt,($2-Queries)/diff;
      Queries=$2
      }
      ' "$@"
   ```
   > 测试工具 sysbench
   [https://github.com/akopytov/sysbench](https://github.com/akopytov/sysbench)

   ```zsh
      # 安装说明 使用实际目录
      ./autogen.sh #回车
      ./configure --with-mysql-includes=/usr/local/mysql/include/ --with-mysql-libs=/usr/local/mysql/lib/
      #回车   
      make #回车 
      makeinstall #回车
      # 常用参数
      --test Fileio # 文件系统I/O测试
      --test cpu # cpu测试
      --test memory # 内存测试
      --test Oltp # 测试指定lua脚本 lua脚本位于 /sysbench/tests/db
      --mysql-db # 指定数据库名
      --mysql-table-engine # 引擎
      --oltp-tables-count # 5.5之前 执行测试表的数量 5.5之后改为lua脚本
      --oltp-table-size # 5.5之前 指定每个表中数据行数 5.5之后改为lua脚本
      --num-threads # 指定测试的并发线程数量
      --max-time # 指定最大测试时间
      --report-interval # 指定间隔多长时间输出一次信息
      --mysql-user # 指定Mysql用户
      --mysql-password #用户密码
      prepare # 测试数据
      run # 进行测试
      cleanup # 清理测试数据
    ```
6. 数据结构设计
   - 减少冗余
   - 减少异常
   - 节约存储空间
   - 提高查询效率
   #### 设计步骤
   - 需求分析 
   - 逻辑设计 业务实体逻辑关系
   - 物理设计 数据库选择 表结构设计
   - 维护优化 索引,数据结构等优化
7. SQL语句优化
#### 数据库设计
> 设计三范式 不一定严格 应以实际应用情况为准
- 第一范式: 字段单一属性没有歧义,基本数据类型,二维表
- 第二范式: 唯一业务主键
- 第三范式: 消除非主属性 对 主属性 的传递依赖(例如学生信息和学院信息分开,主键关联)
> 图书网站示例:
1. 需求分析示例  
   _类型:只销售图书类商品_  
   _功能需求:_    
   - 用户登录  
   a. 必须注册登录后才能网上交易  
   b. 同一时间同一用户登录一台设备(或一个地点)  
   c. 用户必填信息及可选信息  
   - 商品展示
   - 供应商管理
   - 用户管理
   - 商品管理
   - 在线销售  
   _......_
   > 反范式化设计  
   根据实际的需求,允许一定的数据冗余,如订单表中冗余部分用户信息,减少链表查询,订单商品表冗余不分商品信息:  
   订单表: 编号,用户名,日期,金额,物流单号...  
   订单商品表: 订单编号,商品分类,商品名,规格,数量...
   
2. 物理设计
   > 服务器,架构,引擎,配置...  
   > 表数据类型优先级: 占用空间小 > 数字 > 日期/二进制 > 字符(定长用char)
   > datetime:秒,datetime(6):微秒 不依赖时区 ,timestamp:1970-2038年依赖时区
