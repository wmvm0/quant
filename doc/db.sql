CREATE TABLE `ji_jin` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `code` varchar(255) NOT NULL COMMENT '基金代码',
  `name` varchar(255) NOT NULL COMMENT '基金简称',
  `unit_net_value` double(11,4) NOT NULL COMMENT '单位净值',
  `acc_net_value` double(11,4) NOT NULL COMMENT '累计净值',
  `day_incr_rate` double(11,2) NOT NULL COMMENT '日增长率',
  `one_week_incr_rate` double(11,2) NOT NULL COMMENT '近一周增长率',
  `one_month_incr_rate` double(11,2) NOT NULL COMMENT '近一月增长率',
  `three_month_incr_rate` double(11,2) NOT NULL COMMENT '近三月增长率',
  `six_month_incr_rate` double(11,2) NOT NULL COMMENT '近六月增长率',
  `one_year_incr_rate` double(11,2) NOT NULL COMMENT '近一年增长率',
  `two_year_incr_rate` double(11,2) NOT NULL COMMENT '近两年增长率',
  `three_year_incr_rate` double(11,2) NOT NULL COMMENT '近三年增长率',
  `this_year_incr_rate` double(11,2) NOT NULL COMMENT '近年来增长率',
  `all_incr_rate` double(11,2) NOT NULL COMMENT '成立以来增长率',
  `service_charge` double(11,2) NOT NULL DEFAULT '0.00' COMMENT '手续费',
  `ctime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `utime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `date` varchar(255) NOT NULL DEFAULT '' COMMENT '时间',
  `feature_risk_grade_all` int NOT NULL DEFAULT '0' COMMENT '风险等级',
  `feature_risk_grade_same` int NOT NULL DEFAULT '0',
  `feature_update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `feature_trace_index` varchar(255) NOT NULL DEFAULT '',
  `feature_trace_deviation` double(11,2) NOT NULL DEFAULT '0.00',
  `feature_trace_mean_deviation` double(11,2) NOT NULL DEFAULT '0.00',
  `feature_standard_deviation_1year` double(11,2) NOT NULL DEFAULT '0.00',
  `feature_standard_deviation_2year` double(11,2) NOT NULL DEFAULT '0.00',
  `feature_standard_deviation_3year` double(11,2) NOT NULL DEFAULT '0.00',
  `feature_sharpe_ratio_1year` double(11,2) NOT NULL DEFAULT '0.00',
  `feature_sharpe_ratio_2year` double(11,2) NOT NULL DEFAULT '0.00',
  `feature_sharpe_ratio_3year` double(11,2) NOT NULL DEFAULT '0.00',
  `feature_info_ratio_1year` double(11,2) NOT NULL DEFAULT '0.00',
  `feature_info_ratio_2year` double(11,2) NOT NULL DEFAULT '0.00',
  `feature_info_ratio_3year` double(11,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`id`),
  UNIQUE KEY `ji_jin_pk` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=6009 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;