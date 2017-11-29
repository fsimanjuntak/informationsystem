/*This confguration is intended to improve writing performance of MySQL*/
innodb_read_io_threads=4
innodb_write_io_threads=8  #To stress the double write buffer
innodb_buffer_pool_size=20G
innodb_buffer_pool_load_at_startup=ON
innodb_log_file_size = 32M #Small log files, more page flush
innodb_log_files_in_group=2
innodb_file_per_table=1
innodb_log_buffer_size=8M
innodb_flush_method=O_DIRECT
innodb_flush_log_at_trx_commit=0
skip-innodb_doublewrite  #commented or not depending on test  
