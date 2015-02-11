/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50524
Source Host           : localhost:3306
Source Database       : website

Target Server Type    : MYSQL
Target Server Version : 50524
File Encoding         : 65001

Date: 2014-09-01 10:49:45
*/

SET FOREIGN_KEY_CHECKS=0;

DROP SCHEMA IF EXISTS `ZOPS` ;
CREATE SCHEMA IF NOT EXISTS `ZOPS` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `ZOPS` ;

DROP TABLE IF EXISTS `ops_acl` ;

CREATE TABLE IF NOT EXISTS `ops_acl` (
  `operator` VARCHAR(45) NOT NULL COMMENT '申请者',
  `access_num` VARCHAR(8) NOT NULL COMMENT '授权码',
  `ip` VARCHAR(20) NOT NULL COMMENT '申请IP',
  `req_time` DATETIME NOT NULL COMMENT '申请时间',
  PRIMARY KEY (`operator`),
  INDEX `z_acl_1` (`access_num` ASC))
ENGINE = MyISAM
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci
COMMENT = '授权表';

-- ----------------------------
-- Table structure for ops_job
-- ----------------------------
DROP TABLE IF EXISTS `ops_job`;
CREATE TABLE `ops_job` (
  `job_id` varchar(100) NOT NULL COMMENT '作业id',
  `job_type` int(255) NOT NULL DEFAULT '0' COMMENT '0:发布 1:回滚',
  `business` varchar(512) NOT NULL COMMENT '发布业务种类',
  `operator` varchar(50) NOT NULL COMMENT '操作者',
  `create_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建job时间',
  `modify_timestamp` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'job状态更新时间',
  `reviewer` varchar(100) DEFAULT NULL COMMENT '审核人',
  `review_member` varchar(255) NOT NULL COMMENT '审核成员',
  `status` int(11) NOT NULL DEFAULT '0' COMMENT '0:待审核1：已审核2：驳回3：正在执行4：接受成功5：接受失败',
  `ret_code` int(11) DEFAULT '0' COMMENT '返回码',
  `ret_msg` varchar(255) DEFAULT NULL COMMENT '返回信息',
  PRIMARY KEY (`job_id`),
  KEY `z_job_1` (`business`(333)),
  KEY `z_job_2` (`operator`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='作业表';

-- ----------------------------
-- Records of ops_job
-- ----------------------------
INSERT INTO `ops_job` VALUES ('201408271734511409132091', '0', '0', 'admin', '2014-08-27 17:34:51', '2014-08-27 17:34:51', null, '', '3', '0', null);
INSERT INTO `ops_job` VALUES ('201408271952091409140329', '0', '0', 'admin', '2014-08-27 19:52:09', '2014-08-27 19:52:09', null, '', '1', '0', null);
INSERT INTO `ops_job` VALUES ('201408281629251409214565', '0', '', 'admin', '2014-08-28 16:29:25', '2014-08-28 16:29:25', null, '', '1', '0', null);
INSERT INTO `ops_job` VALUES ('201408281652411409215961', '1', '', 'admin', '2014-08-28 16:52:41', '2014-08-28 16:52:41', null, '', '2', '0', null);
INSERT INTO `ops_job` VALUES ('201408281740361409218836', '1', '', 'admin', '2014-08-28 17:40:36', '2014-08-28 17:40:36', null, '', '2', '0', null);
INSERT INTO `ops_job` VALUES ('201408281742081409218928', '1', '', 'admin', '2014-08-28 17:42:08', '2014-08-28 17:42:08', null, '', '1', '0', null);
INSERT INTO `ops_job` VALUES ('201408281758211409219901', '0', '', 'admin', '2014-08-28 17:58:21', '2014-08-28 17:58:21', null, '', '2', '0', null);
INSERT INTO `ops_job` VALUES ('201409011013441409537624', '0', '', 'admin', '2014-09-01 10:13:44', '2014-09-01 10:13:44', null, '', '1', '0', null);

-- ----------------------------
-- Table structure for ops_release
-- ----------------------------
DROP TABLE IF EXISTS `ops_release`;
CREATE TABLE `ops_release` (
  `job_id` varchar(100) NOT NULL COMMENT '任务id',
  `release_type` int(255) NOT NULL DEFAULT '0' COMMENT '0:jetty,1:nginx,3:other',
  `create_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  `operator` varchar(20) NOT NULL COMMENT '操作者',
  `reviewer` varchar(100) DEFAULT NULL COMMENT '审核人',
  `business` text NOT NULL COMMENT '1级业务模块',
  `server_ip` text NOT NULL COMMENT '服务器IP',
  `release_url` varchar(512) NOT NULL COMMENT '发布版本URL',
  `rollback_url` varchar(512) NOT NULL COMMENT '回滚版本URL',
  `review_info` varchar(255) DEFAULT NULL,
  `status` int(255) NOT NULL DEFAULT '0' COMMENT '0:待审核1：已审核 2:驳回',
  PRIMARY KEY (`job_id`),
  KEY `ops_release_1` (`operator`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='发布表';

-- ----------------------------
-- Records of ops_release
-- ----------------------------
INSERT INTO `ops_release` VALUES ('201408271713121409130792', '0', '2014-08-28 14:49:36', 'admin', null, 'ff', 'ff', 'http://122.com', 'http://122.com', 'ok', '1');
INSERT INTO `ops_release` VALUES ('201408271732161409131936', '0', '2014-08-28 00:01:05', 'admin', null, '666', '666', 'http://122.com', 'http://122.com', 'not', '0');
INSERT INTO `ops_release` VALUES ('201408271952091409140329', '0', '2014-08-28 17:39:17', 'admin', null, 'dd', 'dd', 'http://d.com/dd', 'http://d.com/dd', '同意！', '1');
INSERT INTO `ops_release` VALUES ('201408281629251409214565', '1', '2014-08-28 17:34:51', 'admin', null, 'ff', 'dd', 'http://122.com', 'http://122.com', '同意！', '1');
INSERT INTO `ops_release` VALUES ('201408281652411409215961', '1', '2014-08-28 17:37:48', 'admin', null, 'ff', 'dd', 'http://122.com', 'http://122.com', '同意！', '2');
INSERT INTO `ops_release` VALUES ('201408281740361409218836', '0', '2014-08-28 17:41:52', 'admin', null, 'dd', 'dd', 'http://d.com/dd', 'http://d.com/dd', '不同意！', '2');
INSERT INTO `ops_release` VALUES ('201408281742081409218928', '1', '2014-08-28 20:26:25', 'admin', null, 'dd', 'dd', 'http://d.com/dd', 'http://d.com/dd', '同意！', '1');
INSERT INTO `ops_release` VALUES ('201408281758211409219901', '2', '2014-08-28 20:26:38', 'admin', null, 'fd', 'ffd', 'http://122.com', 'http://d.com/dd', '不同意！', '2');
INSERT INTO `ops_release` VALUES ('201409011013441409537624', '0', '2014-09-01 10:13:57', 'admin', null, 'fdd', 'sdfs', 'http://122.com', 'http://d.com/dd', '同意！', '1');

-- ----------------------------
-- Table structure for ops_script
-- ----------------------------
DROP TABLE IF EXISTS `ops_script`;
CREATE TABLE `ops_script` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'id',
  `name` varchar(100) NOT NULL COMMENT '脚本名称',
  `detail` text COMMENT '脚本内容',
  `operator` varchar(50) NOT NULL,
  `create_timestamp` datetime NOT NULL COMMENT '创建时间',
  `modify_timestamp` datetime NOT NULL COMMENT '更新时间',
  `status` int(11) NOT NULL COMMENT '0:不可用1：可用',
  `info` varchar(512) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`),
  KEY `ops_script_1` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='脚本管理表';

-- ----------------------------
-- Records of ops_script
-- ----------------------------
INSERT INTO `ops_script` VALUES ('1', 'test.py', 'dddd', 'chenwenhua', '2014-08-22 10:33:43', '2014-08-22 10:33:45', '0', 'OK');

-- ----------------------------
-- Table structure for ops_task
-- ----------------------------
DROP TABLE IF EXISTS `ops_task`;
CREATE TABLE `ops_task` (
  `task_id` varchar(100) NOT NULL COMMENT '任务id',
  `task_type` int(11) NOT NULL COMMENT '任务类型：0发布;1回滚;2重发;3检查',
  `job_id` varchar(100) NOT NULL COMMENT '母job id',
  `create_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '任务创建时间',
  `modify_timestamp` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '任务状态更新时间',
  `status` int(11) NOT NULL COMMENT '0:正在执行1：执行成功2：执行失败',
  `server_ip` varchar(20) NOT NULL COMMENT '服务器IP',
  `ret_code` int(11) DEFAULT NULL COMMENT '返回码',
  `ret_msg` varchar(255) DEFAULT NULL COMMENT '返回信息',
  `task_proc` TEXT NULL COMMENT '任务执行过程',
  PRIMARY KEY (`task_id`),
  KEY `z_task_1` (`task_type`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='任务表';

-- ----------------------------
-- Records of ops_task
-- ----------------------------
INSERT INTO `ops_task` VALUES ('20140821235266', '1', '201408211115555', '2014-08-21 23:53:07', '2014-08-21 23:53:10', '0', '192.168.1.1', '0', 'ok');

-- ----------------------------
-- Table structure for sys_group_permission
-- ----------------------------
DROP TABLE IF EXISTS `sys_group_permission`;
CREATE TABLE `sys_group_permission` (
  `id` varchar(16) NOT NULL,
  `sys_module_id` varchar(16) NOT NULL,
  `user_group_id` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_group_permission
-- ----------------------------
INSERT INTO `sys_group_permission` VALUES ('3su5s88qo2f0', 'cfq21mb3b2o', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s860t9j0', '3su4khubns50', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3ebgl741d0', '3su3jpusnccg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7uj71vg', '3su4k1or8us0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7ri9uh0', '3su3ihcfti5g', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5g69o29nj0', 'cfq22sc8j20', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7nfvlq0', '3su4kqfheq70', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7kqq56g', '3su29glqjn40', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7jpaf80', '3su2ht4ot6lg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7ife8kg', '3su2htg75fpg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7has650', '3su2htrsm0r0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7h4n49g', '3sbv2rcf12c8', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7f42n7g', '3stjc1n6ifq0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7dgloc0', '3sttkecrkfh0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7c9rnr0', '3stt8aek12gg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s7aivsb0', '3vtrl0a8uo', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s79iiln0', '3sbv3d35se2k', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s78421c0', '3sbv2mfamveo', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s75d8tjg', '3stjblir1bq0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5ujot60p0', '3sbv337029r0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s732topg', '3sbv30pg40a4', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s71vefj0', '3sbv2uecis04', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3su5s6ve4h30', '3sbv2j07uddo', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3ebeu8h9j0', '3t36jvur05ug', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('cga8ek623hc', '3t36khkodu0g', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t36ki9u5lqg', '3t36kdenqil0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t36kicfggu0', 'cga8drdu7jg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3e1qt45rt0', '3t36khkodu0g', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3e254f5520', '3t3e24i6rcu0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3ebf17cjs0', '3t3eb9k8dsbg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3i9290j7n0', '3t3i8mru8vq0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3i92c2qnd0', '3t3i8r9i0jk0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3i92f5273g', '3t3i8vprv5l0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3meneuurj0', '3t3md745t310', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3mengk190g', '3t3mcoufum8g', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3menhko1sg', '3t3mcir946t0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t3menis9lj0', '3t3mchct2m80', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t4pq975og50', '3t4pq6u94avg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('cgfuis3j91o', '3t4vhr7j9ha0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t51oga2hu9g', '3t4vhr7j9ha0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t51ogc48n80', '3t51oceclpng', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('cgg5kr04jo4', '3t51oehn4uj0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t51sce8lre0', '3t4vhr7j9ha0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t51scggv720', '3t51oehn4uj0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t51t0jrm2lg', '3t4vhr7j9ha0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('cgg638rrlhc', '3t51oehn4uj0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t551uccnpa0', '3t551r6tn0v0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t551uepuatg', '3t551tned5ig', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t59666e04b0', '3t595kk3t030', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t59669galmg', '3t59659aft50', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5966b2s6e0', '3t59624maev0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('181oj6nrles', '3t5grhgjjd0g', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs1347tmg', '3t5grjf61ou0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('181oj6p3gi0', '3t5grv0s6gmg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs15m2fi0', '3t5grmfcj3cg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs16ks890', '3t5grl0542i0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs18p8fq0', '3t5gr6hcffm0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs18ssf1g', '3t5gra31gtp0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs19qkleg', '3t5grboj61l0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs1bukmc0', '3t5gre2jlnl0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs1d6sjl0', '3t5grfjekps0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs1e88p90', '3t5gr84r01ig', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs1h38an0', '3t5gqrov3490', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs1h6j4sg', '3t5gqv9uiqp0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs1i9j6p0', '181oisjuh60', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('cghm055rvoo', '3t5gr32r08g0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5gs1kfjai0', '3t5gqtoi26qg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('cghnr4ufq4g', '3t5h5j0923r0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5hefivv4m0', '3t5gr32r08g0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('cghqr89m5t8', 'cghqr6ra54k', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('cghqr8go5u8', '3t5gr32r08g0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission` VALUES ('3t5ich2kacig', '3t5h5j0923r0', '3sbsuljdlov8');

-- ----------------------------
-- Table structure for sys_group_permission2
-- ----------------------------
DROP TABLE IF EXISTS `sys_group_permission2`;
CREATE TABLE `sys_group_permission2` (
  `id` varchar(16) NOT NULL,
  `sys_module_id` varchar(16) NOT NULL,
  `user_group_id` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_group_permission2
-- ----------------------------
INSERT INTO `sys_group_permission2` VALUES ('3su5s88qo2f0', 'cfq21mb3b2o', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s860t9j0', '3su4khubns50', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3ebgl741d0', '3su3jpusnccg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7uj71vg', '3su4k1or8us0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7ri9uh0', '3su3ihcfti5g', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t5g69o29nj0', 'cfq22sc8j20', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7nfvlq0', '3su4kqfheq70', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7kqq56g', '3su29glqjn40', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7jpaf80', '3su2ht4ot6lg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7ife8kg', '3su2htg75fpg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7has650', '3su2htrsm0r0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7h4n49g', '3sbv2rcf12c8', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7f42n7g', '3stjc1n6ifq0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7dgloc0', '3sttkecrkfh0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7c9rnr0', '3stt8aek12gg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s7aivsb0', '3vtrl0a8uo', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s79iiln0', '3sbv3d35se2k', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s78421c0', '3sbv2mfamveo', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s75d8tjg', '3stjblir1bq0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5ujot60p0', '3sbv337029r0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s732topg', '3sbv30pg40a4', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s71vefj0', '3sbv2uecis04', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3su5s6ve4h30', '3sbv2j07uddo', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3ebeu8h9j0', '3t36jvur05ug', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('cga8ek623hc', '3t36khkodu0g', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t36ki9u5lqg', '3t36kdenqil0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t36kicfggu0', 'cga8drdu7jg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3e1qt45rt0', '3t36khkodu0g', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3e254f5520', '3t3e24i6rcu0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3ebf17cjs0', '3t3eb9k8dsbg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3i9290j7n0', '3t3i8mru8vq0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3i92c2qnd0', '3t3i8r9i0jk0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3i92f5273g', '3t3i8vprv5l0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3meneuurj0', '3t3md745t310', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3mengk190g', '3t3mcoufum8g', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3menhko1sg', '3t3mcir946t0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t3menis9lj0', '3t3mchct2m80', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t4pq975og50', '3t4pq6u94avg', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('cgfuis3j91o', '3t4vhr7j9ha0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t51oga2hu9g', '3t4vhr7j9ha0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t51ogc48n80', '3t51oceclpng', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('cgg5kr04jo4', '3t51oehn4uj0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t51sce8lre0', '3t4vhr7j9ha0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t51scggv720', '3t51oehn4uj0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t51t0jrm2lg', '3t4vhr7j9ha0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('cgg638rrlhc', '3t51oehn4uj0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t551uccnpa0', '3t551r6tn0v0', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t551uepuatg', '3t551tned5ig', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t59666e04b0', '3t595kk3t030', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t59669galmg', '3t59659aft50', '3sbsuljdlov8');
INSERT INTO `sys_group_permission2` VALUES ('3t5966b2s6e0', '3t59624maev0', '3sbsuljdlov8');

-- ----------------------------
-- Table structure for sys_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_log`;
CREATE TABLE `sys_log` (
  `id` varchar(16) NOT NULL,
  `log_content` varchar(200) NOT NULL,
  `log_date` datetime NOT NULL,
  `log_type` tinyint(4) NOT NULL DEFAULT '0',
  `user_id` int(10) unsigned NOT NULL,
  `log_ip` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_log
-- ----------------------------

-- ----------------------------
-- Table structure for sys_module
-- ----------------------------
DROP TABLE IF EXISTS `sys_module`;
CREATE TABLE `sys_module` (
  `id` varchar(16) NOT NULL,
  `module_icon` varchar(20) DEFAULT NULL,
  `module_name` varchar(20) NOT NULL,
  `module_parent_id` varchar(16) DEFAULT NULL,
  `module_type` varchar(10) DEFAULT NULL,
  `module_resource` varchar(60) DEFAULT NULL,
  `module_order` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_module
-- ----------------------------
INSERT INTO `sys_module` VALUES ('3sbv2cmqqisg', 'fa-cog', '系统管理', '', 'module', '', '0');
INSERT INTO `sys_module` VALUES ('3sbv2j07uddo', '', '用户管理', '3sbv2cmqqisg', 'page', 'sys_user/index', '1');
INSERT INTO `sys_module` VALUES ('3sbv2mfamveo', '', '用户组管理', '3sbv2cmqqisg', 'page', 'sys_user_group/index', '2');
INSERT INTO `sys_module` VALUES ('3sbv2rcf12c8', '', '模块管理', '3sbv2cmqqisg', 'page', 'sys_module/index', '3');
INSERT INTO `sys_module` VALUES ('3sbv2uecis04', '', '添加用户', '3sbv2j07uddo', 'action', 'sys_user/add', '0');
INSERT INTO `sys_module` VALUES ('3sbv30pg40a4', '', '修改用户', '3sbv2j07uddo', 'action', 'sys_user/edit', '0');
INSERT INTO `sys_module` VALUES ('3sbv337029r0', '', '删除用户', '3sbv2j07uddo', 'action', 'sys_user/delete', '0');
INSERT INTO `sys_module` VALUES ('3sbv3d35se2k', '', '添加组', '3sbv2mfamveo', 'action', 'sys_user_group/add', '0');
INSERT INTO `sys_module` VALUES ('3su4k1or8us0', '', '模板三', '3sc538k8apt8', 'page', 'template/t3', '15');
INSERT INTO `sys_module` VALUES ('3sc538k8apt8', '', '需求管理', '', 'module', '', '2');
INSERT INTO `sys_module` VALUES ('3stjblir1bq0', '', '修改用户状态', '3sbv2j07uddo', 'action', 'sys_user/status', '0');
INSERT INTO `sys_module` VALUES ('3stjc1n6ifq0', '', '删除用户组', '3sbv2mfamveo', 'action', 'sys_user_group/delete', '4');
INSERT INTO `sys_module` VALUES ('3vtrl0a8uo', '', '权限配置', '3sbv2mfamveo', 'action', 'sys_group_permission/config', '0');
INSERT INTO `sys_module` VALUES ('3stt8aek12gg', '', '权限修改', '3sbv2mfamveo', 'action', 'sys_group_permission/change', '0');
INSERT INTO `sys_module` VALUES ('3sttkecrkfh0', '', '修改用户组', '3sbv2mfamveo', 'action', 'sys_user_group/edit', '0');
INSERT INTO `sys_module` VALUES ('3su29glqjn40', '', '模块修改', '3sbv2rcf12c8', 'action', 'sys_module/edit', '0');
INSERT INTO `sys_module` VALUES ('3su2ht4ot6lg', '', '模块添加', '3sbv2rcf12c8', 'action', 'sys_module/add', '0');
INSERT INTO `sys_module` VALUES ('3su2htg75fpg', '', '模块删除', '3sbv2rcf12c8', 'action', 'sys_module/delete', '0');
INSERT INTO `sys_module` VALUES ('3su2htrsm0r0', '', '模块排序', '3sbv2rcf12c8', 'action', 'sys_module/sort', '0');
INSERT INTO `sys_module` VALUES ('3su3ihcfti5g', '', '模板二', '3sc538k8apt8', 'page', 'template/t2', '14');
INSERT INTO `sys_module` VALUES ('3su3jpusnccg', '', '模板一', '3sc538k8apt8', 'page', 'template/t1', '13');
INSERT INTO `sys_module` VALUES ('cfq21mb3b2o', '', '系统报表', '3sc538k8apt8', 'page', 'template/report', '11');
INSERT INTO `sys_module` VALUES ('3su4khubns50', '', '开发工具', '3sc538k8apt8', 'page', 'template/tools', '12');
INSERT INTO `sys_module` VALUES ('3su4kqfheq70', '', '操作日志', '3sbv2cmqqisg', 'page', 'sys_log/index', '4');
INSERT INTO `sys_module` VALUES ('cfq22sc8j20', '', '日志查询', '3su4kqfheq70', 'action', 'sys_log/list', '0');
INSERT INTO `sys_module` VALUES ('3t36jvuqv0eg', '', '运维发布', '', 'module', '', '1');
INSERT INTO `sys_module` VALUES ('3t36jvur05ug', '', '日常发布', '3t36jvuqv0eg', 'page', 'zops/zops_manage/index', '5');
INSERT INTO `sys_module` VALUES ('cga8drdu7jg', '', '任务详情', '3t36jvuqv0eg', 'page', 'zops/zops_detail/index', '6');
INSERT INTO `sys_module` VALUES ('3t36kdenqil0', '', '脚本管理', '3t36jvuqv0eg', 'page', 'zops/zops_script/index', '10');
INSERT INTO `sys_module` VALUES ('3t3e24i6rcu0', '', '发布统计', '3t36jvuqv0eg', 'page', 'zops/zops_statistic/index', '8');
INSERT INTO `sys_module` VALUES ('3t3eb9k8dsbg', '', '拉取数据', '3t36jvur05ug', 'action', 'zops/zops_manage/get_list', '0');
INSERT INTO `sys_module` VALUES ('3t3i8mru8vq0', '', '拉取数据', 'cga8drdu7jg', 'action', 'zops/zops_detail/get_list', '0');
INSERT INTO `sys_module` VALUES ('3t3i8r9i0jk0', '', '拉取数据', '3t36kdenqil0', 'action', 'zops/zops_script/get_list', '0');
INSERT INTO `sys_module` VALUES ('3t3i8vprv5l0', '', '拉取数据', '3t3e24i6rcu0', 'action', 'zops/zops_statistic/get_list', '0');
INSERT INTO `sys_module` VALUES ('3t3mchct2m80', '', '拉取数据', '3su3jpusnccg', 'action', 'template/t1_get_list', '0');
INSERT INTO `sys_module` VALUES ('3t3mcir946t0', '', '增加数据', '3su3jpusnccg', 'action', 'template/t1_add', '0');
INSERT INTO `sys_module` VALUES ('3t3mcoufum8g', '', '删除数据', '3su3jpusnccg', 'action', 'template/t1_del', '0');
INSERT INTO `sys_module` VALUES ('3t3md745t310', '', '修改数据', '3su3jpusnccg', 'action', 'template/t1_edit', '0');
INSERT INTO `sys_module` VALUES ('3t4pq6u94avg', '', '常规操作', '3t36jvuqv0eg', 'page', 'zops/zops_detail/get_list2', '9');
INSERT INTO `sys_module` VALUES ('3t551r6tn0v0', '', '运维发布', '3t36jvur05ug', 'action', 'zops/zops_manage/release', '0');
INSERT INTO `sys_module` VALUES ('3t51oceclpng', '', '发布详情', '3t36jvur05ug', 'action', 'zops/zops_manage/release_list', '0');
INSERT INTO `sys_module` VALUES ('3t551tned5ig', '', '发布审核', '3t36jvur05ug', 'action', 'zops/zops_manage/release_review', '0');
INSERT INTO `sys_module` VALUES ('3t595kk3t030', '', '发布记录', '3t36jvuqv0eg', 'page', 'zops/zops_history/index', '7');
INSERT INTO `sys_module` VALUES ('3t59624maev0', '', '拉取数据', '3t595kk3t030', 'action', 'zops/zops_history/get_list', '0');
INSERT INTO `sys_module` VALUES ('3t59659aft50', '', '发布详情', '3t595kk3t030', 'action', 'zops/zops_history/release_list', '0');
INSERT INTO `sys_module` VALUES ('3t5gqrov3490', '', '用户管理2', '3sbv2cmqqisg', 'page', 'sys_user2/index ', '0');
INSERT INTO `sys_module` VALUES ('3t5gqtoi26qg', '', '添加用户', '3t5gqrov3490', 'action', 'sys_user2/add ', '0');
INSERT INTO `sys_module` VALUES ('3t5gqv9uiqp0', '', '修改用户', '3t5gqrov3490', 'action', 'sys_user2/edit ', '0');
INSERT INTO `sys_module` VALUES ('181oisjuh60', '', '删除用户', '3t5gqrov3490', 'action', 'sys_user2/delete ', '0');
INSERT INTO `sys_module` VALUES ('3t5gr32r08g0', '', '修改用户状态', '3t5gqrov3490', 'action', 'sys_user2/status ', '0');
INSERT INTO `sys_module` VALUES ('3t5gr6hcffm0', '', '用户组管理2', '3sbv2cmqqisg', 'page', 'sys_user_group2/index ', '0');
INSERT INTO `sys_module` VALUES ('3t5gr84r01ig', '', '添加组', '3t5gr6hcffm0', 'action', 'sys_user_group2/add ', '0');
INSERT INTO `sys_module` VALUES ('3t5gra31gtp0', '', '权限配置', '3t5gr6hcffm0', 'action', 'sys_group_permission2/config ', '0');
INSERT INTO `sys_module` VALUES ('3t5grboj61l0', '', '权限修改', '3t5gr6hcffm0', 'action', 'sys_group_permission2/change ', '0');
INSERT INTO `sys_module` VALUES ('3t5gre2jlnl0', '', '修改用户组', '3t5gr6hcffm0', 'action', 'sys_user_group2/edit ', '0');
INSERT INTO `sys_module` VALUES ('3t5grfjekps0', '', '删除用户组', '3t5gr6hcffm0', 'action', 'sys_user_group2/delete ', '0');
INSERT INTO `sys_module` VALUES ('3t5grhgjjd0g', '', '模块管理2', '3sbv2cmqqisg', 'page', 'sys_module2/index ', '0');
INSERT INTO `sys_module` VALUES ('3t5grjf61ou0', '', '模块修改', '3t5grhgjjd0g', 'action', 'sys_module2/edit ', '0');
INSERT INTO `sys_module` VALUES ('3t5grl0542i0', '', '模块添加', '3t5grhgjjd0g', 'action', 'sys_module2/add ', '0');
INSERT INTO `sys_module` VALUES ('3t5grmfcj3cg', '', '模块删除', '3t5grhgjjd0g', 'action', 'sys_module2/delete ', '0');
INSERT INTO `sys_module` VALUES ('3t5grv0s6gmg', '', '模块排序', '3t5grhgjjd0g', 'action', 'sys_module2/sort ', '0');
INSERT INTO `sys_module` VALUES ('3t5h5j0923r0', '', '拉取数据', '3t5gr6hcffm0', 'action', 'sys_user_group2/get_list', '0');
INSERT INTO `sys_module` VALUES ('cghqr6ra54k', '', '拉取数据', '3t5gqrov3490', 'action', 'sys_user2/get_list', '0');

-- ----------------------------
-- Table structure for sys_module2
-- ----------------------------
DROP TABLE IF EXISTS `sys_module2`;
CREATE TABLE `sys_module2` (
  `id` varchar(16) NOT NULL,
  `module_icon` varchar(20) DEFAULT NULL,
  `module_name` varchar(20) NOT NULL,
  `module_parent_id` varchar(16) DEFAULT NULL,
  `module_type` varchar(10) DEFAULT NULL,
  `module_resource` varchar(60) DEFAULT NULL,
  `module_order` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_module2
-- ----------------------------
INSERT INTO `sys_module2` VALUES ('3sbv2cmqqisg', 'fa-cog', '系统管理', '', 'module', '', '0');
INSERT INTO `sys_module2` VALUES ('3sbv2j07uddo', '', '用户管理', '3sbv2cmqqisg', 'page', 'sys_user/index', '0');
INSERT INTO `sys_module2` VALUES ('3sbv2mfamveo', '', '用户组管理', '3sbv2cmqqisg', 'page', 'sys_user_group/index', '1');
INSERT INTO `sys_module2` VALUES ('3sbv2rcf12c8', '', '模块管理', '3sbv2cmqqisg', 'page', 'sys_module/index', '2');
INSERT INTO `sys_module2` VALUES ('3sbv2uecis04', '', '添加用户', '3sbv2j07uddo', 'action', 'sys_user/add', '0');
INSERT INTO `sys_module2` VALUES ('3sbv30pg40a4', '', '修改用户', '3sbv2j07uddo', 'action', 'sys_user/edit', '0');
INSERT INTO `sys_module2` VALUES ('3sbv337029r0', '', '删除用户', '3sbv2j07uddo', 'action', 'sys_user/delete', '0');
INSERT INTO `sys_module2` VALUES ('3sbv3d35se2k', '', '添加组', '3sbv2mfamveo', 'action', 'sys_user_group/add', '0');
INSERT INTO `sys_module2` VALUES ('3su4k1or8us0', '', '模板三', '3sc538k8apt8', 'page', 'template/t3', '14');
INSERT INTO `sys_module2` VALUES ('3sc538k8apt8', '', '需求管理', '', 'module', '', '2');
INSERT INTO `sys_module2` VALUES ('3stjblir1bq0', '', '修改用户状态', '3sbv2j07uddo', 'action', 'sys_user/status', '0');
INSERT INTO `sys_module2` VALUES ('3stjc1n6ifq0', '', '删除用户组', '3sbv2mfamveo', 'action', 'sys_user_group/delete', '4');
INSERT INTO `sys_module2` VALUES ('3vtrl0a8uo', '', '权限配置', '3sbv2mfamveo', 'action', 'sys_group_permission/config', '0');
INSERT INTO `sys_module2` VALUES ('3stt8aek12gg', '', '权限修改', '3sbv2mfamveo', 'action', 'sys_group_permission/change', '0');
INSERT INTO `sys_module2` VALUES ('3sttkecrkfh0', '', '修改用户组', '3sbv2mfamveo', 'action', 'sys_user_group/edit', '0');
INSERT INTO `sys_module2` VALUES ('3su29glqjn40', '', '模块修改', '3sbv2rcf12c8', 'action', 'sys_module/edit', '0');
INSERT INTO `sys_module2` VALUES ('3su2ht4ot6lg', '', '模块添加', '3sbv2rcf12c8', 'action', 'sys_module/add', '0');
INSERT INTO `sys_module2` VALUES ('3su2htg75fpg', '', '模块删除', '3sbv2rcf12c8', 'action', 'sys_module/delete', '0');
INSERT INTO `sys_module2` VALUES ('3su2htrsm0r0', '', '模块排序', '3sbv2rcf12c8', 'action', 'sys_module/sort', '0');
INSERT INTO `sys_module2` VALUES ('3su3ihcfti5g', '', '模板二', '3sc538k8apt8', 'page', 'template/t2', '13');
INSERT INTO `sys_module2` VALUES ('3su3jpusnccg', '', '模板一', '3sc538k8apt8', 'page', 'template/t1', '12');
INSERT INTO `sys_module2` VALUES ('cfq21mb3b2o', '', '系统报表', '3sc538k8apt8', 'page', 'template/report', '10');
INSERT INTO `sys_module2` VALUES ('3su4khubns50', '', '开发工具', '3sc538k8apt8', 'page', 'template/tools', '11');
INSERT INTO `sys_module2` VALUES ('3su4kqfheq70', '', '操作日志', '3sbv2cmqqisg', 'page', 'sys_log/index', '3');
INSERT INTO `sys_module2` VALUES ('cfq22sc8j20', '', '日志查询', '3su4kqfheq70', 'action', 'sys_log/list', '0');
INSERT INTO `sys_module2` VALUES ('3t36jvuqv0eg', '', '运维发布', '', 'module', '', '1');
INSERT INTO `sys_module2` VALUES ('3t36jvur05ug', '', '日常发布', '3t36jvuqv0eg', 'page', 'zops/zops_manage/index', '4');
INSERT INTO `sys_module2` VALUES ('cga8drdu7jg', '', '任务详情', '3t36jvuqv0eg', 'page', 'zops/zops_detail/index', '5');
INSERT INTO `sys_module2` VALUES ('3t36kdenqil0', '', '脚本管理', '3t36jvuqv0eg', 'page', 'zops/zops_script/index', '9');
INSERT INTO `sys_module2` VALUES ('3t3e24i6rcu0', '', '发布统计', '3t36jvuqv0eg', 'page', 'zops/zops_statistic/index', '7');
INSERT INTO `sys_module2` VALUES ('3t3eb9k8dsbg', '', '拉取数据', '3t36jvur05ug', 'action', 'zops/zops_manage/get_list', '0');
INSERT INTO `sys_module2` VALUES ('3t3i8mru8vq0', '', '拉取数据', 'cga8drdu7jg', 'action', 'zops/zops_detail/get_list', '0');
INSERT INTO `sys_module2` VALUES ('3t3i8r9i0jk0', '', '拉取数据', '3t36kdenqil0', 'action', 'zops/zops_script/get_list', '0');
INSERT INTO `sys_module2` VALUES ('3t3i8vprv5l0', '', '拉取数据', '3t3e24i6rcu0', 'action', 'zops/zops_statistic/get_list', '0');
INSERT INTO `sys_module2` VALUES ('3t3mchct2m80', '', '拉取数据', '3su3jpusnccg', 'action', 'template/t1_get_list', '0');
INSERT INTO `sys_module2` VALUES ('3t3mcir946t0', '', '增加数据', '3su3jpusnccg', 'action', 'template/t1_add', '0');
INSERT INTO `sys_module2` VALUES ('3t3mcoufum8g', '', '删除数据', '3su3jpusnccg', 'action', 'template/t1_del', '0');
INSERT INTO `sys_module2` VALUES ('3t3md745t310', '', '修改数据', '3su3jpusnccg', 'action', 'template/t1_edit', '0');
INSERT INTO `sys_module2` VALUES ('3t4pq6u94avg', '', '常规操作', '3t36jvuqv0eg', 'page', 'zops/zops_detail/get_list2', '8');
INSERT INTO `sys_module2` VALUES ('3t551r6tn0v0', '', '运维发布', '3t36jvur05ug', 'action', 'zops/zops_manage/release', '0');
INSERT INTO `sys_module2` VALUES ('3t51oceclpng', '', '发布详情', '3t36jvur05ug', 'action', 'zops/zops_manage/release_list', '0');
INSERT INTO `sys_module2` VALUES ('3t551tned5ig', '', '发布审核', '3t36jvur05ug', 'action', 'zops/zops_manage/release_review', '0');
INSERT INTO `sys_module2` VALUES ('3t595kk3t030', '', '发布记录', '3t36jvuqv0eg', 'page', 'zops/zops_history/index', '6');
INSERT INTO `sys_module2` VALUES ('3t59624maev0', '', '拉取数据', '3t595kk3t030', 'action', 'zops/zops_history/get_list', '0');
INSERT INTO `sys_module2` VALUES ('3t59659aft50', '', '发布详情', '3t595kk3t030', 'action', 'zops/zops_history/release_list', '0');

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user` (
  `id` varchar(16) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(45) NOT NULL,
  `truename` varchar(45) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `createdate` datetime NOT NULL,
  `sys_group_id` varchar(16) NOT NULL,
  `flag_valid` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES ('3su64lrobd60', 'chenwenhua', '082e51117225bf0b306d88cad30ca8af', '陈文华', 'wenhua@meizu.com', '0000-00-00 00:00:00', '3sbsuljdlov8', '1');
INSERT INTO `sys_user` VALUES ('3sc4efprua2s', 'admin', '9b3d317e1007d5aaf21b213a0ef7c019', '超人', 'admin@meizu.com', '0000-00-00 00:00:00', '3sbsuljdlov8', '1');

-- ----------------------------
-- Table structure for sys_user2
-- ----------------------------
DROP TABLE IF EXISTS `sys_user2`;
CREATE TABLE `sys_user2` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL COMMENT '名字拼音',
  `password` varchar(45) NOT NULL COMMENT '密码',
  `truename` varchar(45) NOT NULL COMMENT '中文名',
  `email` varchar(80) NOT NULL COMMENT 'email',
  `createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `group_id` varchar(255) NOT NULL COMMENT '组ID',
  `flag_valid` int(11) NOT NULL COMMENT '0:无效，1：有效',
  PRIMARY KEY (`id`,`username`,`email`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  KEY `k_group_id` (`group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of sys_user2
-- ----------------------------
INSERT INTO `sys_user2` VALUES ('1', 'chenwenhua', '082e51117225bf0b306d88cad30ca8af', '陈文华', 'wenhua@meizu.com', '2014-08-29 20:52:32', '1', '1');
INSERT INTO `sys_user2` VALUES ('2', 'admin', '9b3d317e1007d5aaf21b213a0ef7c019', '超人', 'admin@meizu.com', '2014-08-29 20:52:35', '1', '1');

-- ----------------------------
-- Table structure for sys_user_group
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_group`;
CREATE TABLE `sys_user_group` (
  `id` varchar(24) NOT NULL,
  `group_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_user_group
-- ----------------------------
INSERT INTO `sys_user_group` VALUES ('3sbsuljdlov8', '超级管理员');
INSERT INTO `sys_user_group` VALUES ('3sbsv5h9dr80', '架构组');
INSERT INTO `sys_user_group` VALUES ('3sbt025107mc', '运维组');

-- ----------------------------
-- Table structure for sys_user_group2
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_group2`;
CREATE TABLE `sys_user_group2` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `group_name` varchar(40) NOT NULL COMMENT '组名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_user_group2
-- ----------------------------
INSERT INTO `sys_user_group2` VALUES ('1', '超级管理员');
INSERT INTO `sys_user_group2` VALUES ('2', '架构组');
INSERT INTO `sys_user_group2` VALUES ('3', '运维组');
INSERT INTO `sys_user_group2` VALUES ('6', 'test');

-- ----------------------------
-- Table structure for user1
-- ----------------------------
DROP TABLE IF EXISTS `user1`;
CREATE TABLE `user1` (
  `day` date NOT NULL,
  `kuser1` char(50) NOT NULL DEFAULT '0',
  `kuser2` char(50) NOT NULL DEFAULT '0',
  `kuser3` char(50) NOT NULL DEFAULT '0',
  `kuser4` char(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`day`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user1
-- ----------------------------
INSERT INTO `user1` VALUES ('2011-06-22', '8571', '202047', '1140', '2297');
INSERT INTO `user1` VALUES ('2011-06-23', '9019', '203498', '1257', '2419');
INSERT INTO `user1` VALUES ('2011-06-24', '10046', '242417', '1533', '2680');
INSERT INTO `user1` VALUES ('2011-06-25', '14456', '321423', '1965', '3754');
INSERT INTO `user1` VALUES ('2011-06-26', '14640', '330658', '1909', '3895');
INSERT INTO `user1` VALUES ('2011-06-27', '14377', '317193', '1766', '3687');
INSERT INTO `user1` VALUES ('2011-06-28', '15499', '325570', '1994', '4047');
INSERT INTO `user1` VALUES ('2011-06-29', '14316', '314293', '1908', '3801');
INSERT INTO `user1` VALUES ('2011-06-30', '14406', '308776', '1727', '3651');
INSERT INTO `user1` VALUES ('2011-07-02', '17051', '344326', '1917', '3812');
INSERT INTO `user1` VALUES ('2011-07-03', '16460', '342718', '2308', '3888');
INSERT INTO `user1` VALUES ('2011-07-04', '14955', '326814', '1892', '3643');
INSERT INTO `user1` VALUES ('2011-07-05', '15508', '327115', '1788', '3732');
INSERT INTO `user1` VALUES ('2011-07-06', '16655', '327856', '1811', '3525');
INSERT INTO `user1` VALUES ('2011-07-07', '15642', '332969', '1772', '3703');
INSERT INTO `user1` VALUES ('2011-07-08', '15367', '330749', '1882', '3524');
INSERT INTO `user1` VALUES ('2011-07-09', '16074', '348222', '1919', '3745');
INSERT INTO `user1` VALUES ('2011-07-10', '17266', '359325', '1994', '3996');
INSERT INTO `user1` VALUES ('2011-07-11', '17033', '348871', '1793', '3983');
INSERT INTO `user1` VALUES ('2011-07-12', '16431', '349366', '1829', '3875');
INSERT INTO `user1` VALUES ('2011-07-13', '16718', '347150', '1947', '3860');
INSERT INTO `user1` VALUES ('2011-07-14', '16701', '359732', '1913', '3917');
INSERT INTO `user1` VALUES ('2011-07-15', '17148', '357542', '1897', '4044');
INSERT INTO `user1` VALUES ('2011-07-16', '17731', '368911', '1898', '4041');
INSERT INTO `user1` VALUES ('2011-07-17', '18570', '375386', '1938', '4043');
INSERT INTO `user1` VALUES ('2011-07-18', '17858', '364662', '1858', '4064');
INSERT INTO `user1` VALUES ('2011-07-19', '17149', '355339', '1867', '3807');
INSERT INTO `user1` VALUES ('2011-07-20', '16955', '349229', '1927', '3806');
INSERT INTO `user1` VALUES ('2011-07-21', '17121', '357787', '2065', '4041');
INSERT INTO `user1` VALUES ('2011-07-22', '17725', '354198', '1954', '3954');
INSERT INTO `user1` VALUES ('2011-07-23', '18548', '378172', '2014', '4102');
INSERT INTO `user1` VALUES ('2011-07-24', '19411', '390029', '2092', '4284');
INSERT INTO `user1` VALUES ('2011-07-25', '18830', '383333', '2037', '4133');
INSERT INTO `user1` VALUES ('2011-07-26', '18355', '374210', '2167', '4004');
INSERT INTO `user1` VALUES ('2011-07-27', '18791', '362734', '2074', '3782');
INSERT INTO `user1` VALUES ('2011-07-28', '17784', '366756', '1895', '3874');
INSERT INTO `user1` VALUES ('2011-07-29', '17957', '363397', '2142', '3906');
INSERT INTO `user1` VALUES ('2011-07-30', '19022', '376331', '2146', '4037');
INSERT INTO `user1` VALUES ('2011-07-31', '19608', '380174', '1966', '3797');
INSERT INTO `user1` VALUES ('2011-08-01', '20173', '388294', '2053', '4011');
INSERT INTO `user1` VALUES ('2011-08-02', '18603', '377119', '2197', '4077');
INSERT INTO `user1` VALUES ('2011-08-03', '17956', '363424', '2375', '3977');
INSERT INTO `user1` VALUES ('2011-08-04', '19480', '361670', '1891', '3650');
INSERT INTO `user1` VALUES ('2011-08-05', '18436', '354683', '2085', '3444');
INSERT INTO `user1` VALUES ('2011-08-06', '19143', '368943', '1989', '3649');
INSERT INTO `user1` VALUES ('2011-08-07', '19839', '367982', '2169', '3658');
INSERT INTO `user1` VALUES ('2011-08-08', '17825', '344485', '1911', '3508');
INSERT INTO `user1` VALUES ('2011-08-09', '17811', '329444', '1789', '3469');
INSERT INTO `user1` VALUES ('2011-08-10', '16946', '324650', '1803', '3372');
INSERT INTO `user1` VALUES ('2011-08-11', '16171', '321201', '1972', '3234');
INSERT INTO `user1` VALUES ('2011-08-12', '16576', '317168', '1753', '3175');
INSERT INTO `user1` VALUES ('2011-08-13', '17061', '327097', '1962', '3380');
INSERT INTO `user1` VALUES ('2011-08-14', '17421', '331866', '1926', '3474');
INSERT INTO `user1` VALUES ('2011-08-15', '16032', '311018', '1701', '3114');
INSERT INTO `user1` VALUES ('2011-08-16', '16091', '306315', '1831', '2824');
INSERT INTO `user1` VALUES ('2011-08-17', '15196', '302935', '1678', '2917');
INSERT INTO `user1` VALUES ('2011-08-18', '15737', '293175', '1641', '2902');
INSERT INTO `user1` VALUES ('2011-08-19', '15404', '296754', '1637', '2900');
INSERT INTO `user1` VALUES ('2011-08-20', '16421', '310972', '1778', '2953');
INSERT INTO `user1` VALUES ('2011-08-21', '17517', '313213', '1804', '3027');
INSERT INTO `user1` VALUES ('2011-08-22', '15480', '297763', '1609', '2846');
INSERT INTO `user1` VALUES ('2011-08-23', '16487', '292394', '1717', '2876');
INSERT INTO `user1` VALUES ('2011-08-24', '16327', '300076', '1615', '3009');
INSERT INTO `user1` VALUES ('2011-08-25', '16269', '297205', '1766', '2989');
INSERT INTO `user1` VALUES ('2011-08-26', '16219', '291550', '1657', '2911');
INSERT INTO `user1` VALUES ('2011-08-27', '17131', '309124', '1734', '2993');
INSERT INTO `user1` VALUES ('2011-08-28', '18289', '318570', '1807', '3316');
INSERT INTO `user1` VALUES ('2011-08-29', '16645', '303942', '1718', '2950');
INSERT INTO `user1` VALUES ('2011-08-30', '16885', '299559', '1632', '3149');
INSERT INTO `user1` VALUES ('2011-08-31', '16910', '307169', '1783', '3063');
INSERT INTO `user1` VALUES ('2011-09-01', '17783', '326885', '1782', '3206');
INSERT INTO `user1` VALUES ('2011-09-02', '16975', '319638', '1857', '3082');
INSERT INTO `user1` VALUES ('2011-09-03', '25892', '388899', '2906', '4452');
INSERT INTO `user1` VALUES ('2011-09-04', '24549', '348092', '2081', '3602');
INSERT INTO `user1` VALUES ('2011-09-05', '16626', '309495', '1783', '2959');
INSERT INTO `user1` VALUES ('2011-09-06', '16168', '309932', '1732', '3033');
INSERT INTO `user1` VALUES ('2011-09-07', '16868', '309429', '1838', '3090');
INSERT INTO `user1` VALUES ('2011-09-08', '16574', '304088', '1870', '2924');
INSERT INTO `user1` VALUES ('2011-09-09', '16395', '309506', '1929', '2813');
INSERT INTO `user1` VALUES ('2011-09-10', '19704', '335611', '1975', '3261');
INSERT INTO `user1` VALUES ('2011-09-11', '20744', '342179', '2104', '3513');
INSERT INTO `user1` VALUES ('2011-09-12', '20550', '352683', '2056', '3573');
INSERT INTO `user1` VALUES ('2011-09-13', '17255', '314749', '1785', '3210');
INSERT INTO `user1` VALUES ('2011-09-14', '17186', '316242', '1788', '2967');
INSERT INTO `user1` VALUES ('2011-09-15', '16392', '308988', '1739', '2932');
INSERT INTO `user1` VALUES ('2011-09-16', '17497', '315431', '1779', '2987');
INSERT INTO `user1` VALUES ('2011-09-17', '20172', '344200', '1989', '3312');
INSERT INTO `user1` VALUES ('2011-09-18', '19932', '343001', '2030', '3302');
INSERT INTO `user1` VALUES ('2011-09-19', '17076', '308253', '1790', '2977');
INSERT INTO `user1` VALUES ('2011-09-20', '16697', '307790', '1849', '2975');
INSERT INTO `user1` VALUES ('2011-09-21', '15967', '304472', '1805', '2881');
INSERT INTO `user1` VALUES ('2011-09-22', '16561', '306183', '1883', '2837');
INSERT INTO `user1` VALUES ('2011-09-23', '17645', '306246', '1933', '2958');
INSERT INTO `user1` VALUES ('2011-09-24', '19764', '336657', '1997', '3150');
INSERT INTO `user1` VALUES ('2011-09-25', '20578', '336503', '2279', '3360');
INSERT INTO `user1` VALUES ('2011-09-26', '14884', '257558', '1515', '2535');
INSERT INTO `user1` VALUES ('2011-09-27', '18002', '313127', '1841', '2984');
INSERT INTO `user1` VALUES ('2011-09-28', '18381', '317784', '1957', '3119');
INSERT INTO `user1` VALUES ('2011-09-29', '18939', '311378', '2069', '2971');
INSERT INTO `user1` VALUES ('2011-09-30', '19922', '321487', '2055', '3135');
INSERT INTO `user1` VALUES ('2011-10-01', '24484', '357797', '2293', '4006');
INSERT INTO `user1` VALUES ('2011-10-02', '22759', '333939', '2372', '3441');
INSERT INTO `user1` VALUES ('2011-10-03', '23037', '324450', '2096', '3221');
INSERT INTO `user1` VALUES ('2011-10-04', '21396', '323930', '2004', '3246');
INSERT INTO `user1` VALUES ('2011-10-05', '20671', '330835', '2066', '3176');
INSERT INTO `user1` VALUES ('2011-10-06', '22204', '346953', '1967', '3438');
INSERT INTO `user1` VALUES ('2011-10-07', '22743', '348973', '2181', '3447');
INSERT INTO `user1` VALUES ('2011-10-08', '21201', '339126', '2134', '3417');
INSERT INTO `user1` VALUES ('2011-10-09', '20831', '345892', '2062', '3395');
INSERT INTO `user1` VALUES ('2011-10-10', '21156', '339323', '1893', '3400');
INSERT INTO `user1` VALUES ('2011-10-11', '20760', '337308', '1853', '3264');
INSERT INTO `user1` VALUES ('2011-10-12', '21564', '336935', '1840', '3218');
INSERT INTO `user1` VALUES ('2011-10-13', '21068', '336272', '1798', '1954701462');
INSERT INTO `user1` VALUES ('2011-10-14', '22184', '332544', '1815', '3249');
INSERT INTO `user1` VALUES ('2011-10-15', '24873', '358957', '1919', '3447');
INSERT INTO `user1` VALUES ('2011-10-16', '25224', '363158', '2156', '3611');
INSERT INTO `user1` VALUES ('2011-10-17', '22047', '333710', '1955', '3131');
INSERT INTO `user1` VALUES ('2011-10-18', '21464', '332229', '1819', '3183');
INSERT INTO `user1` VALUES ('2011-10-19', '22068', '334469', '1965', '3438');
INSERT INTO `user1` VALUES ('2011-10-20', '21669', '339389', '1812', '3381');
INSERT INTO `user1` VALUES ('2011-10-21', '17202', '258710', '1558', '2554');
INSERT INTO `user1` VALUES ('2011-10-22', '24492', '345330', '2287', '3420');
INSERT INTO `user1` VALUES ('2011-10-23', '26815', '372179', '2366', '3674');
INSERT INTO `user1` VALUES ('2011-10-24', '22841', '341907', '2093', '3377');
INSERT INTO `user1` VALUES ('2011-10-25', '23800', '334757', '1966', '3272');
INSERT INTO `user1` VALUES ('2011-10-26', '22159', '332088', '1995', '3472');
INSERT INTO `user1` VALUES ('2011-10-27', '21971', '333630', '2004', '3323');
INSERT INTO `user1` VALUES ('2011-10-28', '23501', '334758', '2028', '3149');
INSERT INTO `user1` VALUES ('2011-10-29', '26690', '370290', '2307', '3648');
INSERT INTO `user1` VALUES ('2011-10-30', '25982', '370626', '2198', '3666');
INSERT INTO `user1` VALUES ('2011-10-31', '22940', '339893', '2114', '3305');
INSERT INTO `user1` VALUES ('2011-11-01', '23722', '350374', '2017', '3486');
INSERT INTO `user1` VALUES ('2011-11-02', '23709', '349397', '2102', '3499');
INSERT INTO `user1` VALUES ('2011-11-03', '23263', '354734', '2115', '3563');
INSERT INTO `user1` VALUES ('2011-11-04', '27148', '393588', '2525', '4245');
INSERT INTO `user1` VALUES ('2011-11-05', '31351', '422833', '2759', '4367');
INSERT INTO `user1` VALUES ('2011-11-06', '29693', '413326', '2712', '4166');
INSERT INTO `user1` VALUES ('2011-11-07', '25217', '371761', '2427', '3687');
INSERT INTO `user1` VALUES ('2011-11-08', '24417', '367968', '2305', '3706');
INSERT INTO `user1` VALUES ('2011-11-09', '23875', '362167', '2297', '3628');
INSERT INTO `user1` VALUES ('2011-11-10', '22952', '338279', '2119', '3429');
INSERT INTO `user1` VALUES ('2011-11-11', '24264', '355308', '2284', '4178');
INSERT INTO `user1` VALUES ('2011-11-12', '27021', '366489', '2292', '3703');
INSERT INTO `user1` VALUES ('2011-11-13', '27180', '381973', '2566', '3714');
INSERT INTO `user1` VALUES ('2011-11-14', '23962', '351148', '2161', '3393');
INSERT INTO `user1` VALUES ('2011-11-15', '23822', '350331', '2145', '3354');
INSERT INTO `user1` VALUES ('2011-11-16', '23835', '367038', '2307', '3531');
INSERT INTO `user1` VALUES ('2011-11-17', '25212', '377359', '2354', '3754');
INSERT INTO `user1` VALUES ('2011-11-18', '26401', '378373', '2354', '3778');
INSERT INTO `user1` VALUES ('2011-11-19', '30326', '405494', '2652', '4238');
INSERT INTO `user1` VALUES ('2011-11-20', '29228', '396770', '2454', '3961');
INSERT INTO `user1` VALUES ('2011-11-21', '24596', '364502', '2268', '3459');
INSERT INTO `user1` VALUES ('2011-11-22', '24982', '368587', '2185', '3679');
INSERT INTO `user1` VALUES ('2011-11-24', '25969', '378290', '2562', '3862');
INSERT INTO `user1` VALUES ('2011-11-25', '26343', '371320', '2154', '3733');
INSERT INTO `user1` VALUES ('2011-11-26', '31475', '410225', '2600', '4404');
INSERT INTO `user1` VALUES ('2011-11-27', '30989', '412249', '2715', '4159');
INSERT INTO `user1` VALUES ('2011-11-28', '26455', '379612', '2260', '3697');
INSERT INTO `user1` VALUES ('2011-11-29', '24530', '346339', '2217', '3495');
INSERT INTO `user1` VALUES ('2011-11-30', '19592', '285306', '1737', '2871');
INSERT INTO `user1` VALUES ('2011-12-01', '26303', '371105', '2253', '3645');
INSERT INTO `user1` VALUES ('2011-12-02', '25112', '360114', '2251', '3752');
INSERT INTO `user1` VALUES ('2011-12-03', '29368', '388728', '2551', '3909');
INSERT INTO `user1` VALUES ('2011-12-04', '30054', '388833', '2591', '4159');
INSERT INTO `user1` VALUES ('2011-12-05', '25064', '363333', '2243', '3889');
INSERT INTO `user1` VALUES ('2011-12-06', '25518', '361425', '2235', '3823');
INSERT INTO `user1` VALUES ('2011-12-07', '25955', '368869', '2414', '3723');
INSERT INTO `user1` VALUES ('2011-12-08', '25868', '361111', '2242', '3709');
INSERT INTO `user1` VALUES ('2011-12-09', '25940', '359602', '2216', '3595');
INSERT INTO `user1` VALUES ('2011-12-10', '31628', '393754', '2481', '4095');
INSERT INTO `user1` VALUES ('2011-12-11', '31267', '396357', '2512', '4651');
INSERT INTO `user1` VALUES ('2011-12-12', '25983', '347002', '2210', '3709');
INSERT INTO `user1` VALUES ('2011-12-13', '25330', '355490', '2283', '3760');
INSERT INTO `user1` VALUES ('2011-12-14', '26574', '361904', '2306', '3777');
INSERT INTO `user1` VALUES ('2011-12-15', '26084', '360895', '2237', '3698');
INSERT INTO `user1` VALUES ('2011-12-16', '28628', '368396', '2373', '3717');
INSERT INTO `user1` VALUES ('2011-12-17', '33826', '404171', '2593', '4347');
INSERT INTO `user1` VALUES ('2011-12-18', '33305', '411393', '2524', '4436');
INSERT INTO `user1` VALUES ('2011-12-19', '28235', '373054', '2438', '3842');
INSERT INTO `user1` VALUES ('2011-12-20', '28534', '388939', '2354', '4157');
INSERT INTO `user1` VALUES ('2011-12-21', '30746', '418739', '2726', '4609');
INSERT INTO `user1` VALUES ('2011-12-22', '23529', '318239', '2070', '3323');
INSERT INTO `user1` VALUES ('2011-12-23', '31233', '408862', '2516', '4268');
INSERT INTO `user1` VALUES ('2011-12-24', '36037', '441817', '2812', '4953');
INSERT INTO `user1` VALUES ('2011-12-25', '37583', '467328', '3028', '4831');
INSERT INTO `user1` VALUES ('2011-12-26', '31759', '418722', '2839', '4408');
INSERT INTO `user1` VALUES ('2011-12-27', '32719', '420293', '2864', '4451');
INSERT INTO `user1` VALUES ('2011-12-28', '33570', '414036', '2616', '4403');
INSERT INTO `user1` VALUES ('2011-12-29', '32055', '419936', '2717', '4690');
INSERT INTO `user1` VALUES ('2011-12-30', '33166', '429787', '2700', '4547');
INSERT INTO `user1` VALUES ('2011-12-31', '37982', '470097', '3217', '5025');
INSERT INTO `user1` VALUES ('2012-01-01', '50058', '528705', '3660', '5862');
INSERT INTO `user1` VALUES ('2012-01-02', '42377', '503257', '3663', '5423');
INSERT INTO `user1` VALUES ('2012-01-03', '39948', '491383', '3382', '5333');
INSERT INTO `user1` VALUES ('2012-01-04', '35945', '442541', '2965', '4834');
INSERT INTO `user1` VALUES ('2012-01-05', '31831', '417058', '2874', '4380');
INSERT INTO `user1` VALUES ('2012-01-06', '31774', '388805', '2654', '3993');
INSERT INTO `user1` VALUES ('2012-01-07', '37259', '459360', '3244', '5113');
INSERT INTO `user1` VALUES ('2012-01-08', '34266', '429532', '2943', '4704');
INSERT INTO `user1` VALUES ('2012-01-09', '34445', '437788', '2999', '4745');
INSERT INTO `user1` VALUES ('2012-01-10', '32507', '415167', '2832', '4585');
INSERT INTO `user1` VALUES ('2012-01-11', '36454', '455142', '3286', '4919');
INSERT INTO `user1` VALUES ('2012-01-12', '38657', '462812', '3324', '4778');
INSERT INTO `user1` VALUES ('2012-01-13', '37013', '441104', '3208', '4883');
INSERT INTO `user1` VALUES ('2012-01-14', '43157', '503496', '3606', '5526');
INSERT INTO `user1` VALUES ('2012-01-15', '47256', '515021', '3873', '5947');
INSERT INTO `user1` VALUES ('2012-01-16', '41948', '466981', '3283', '5201');
INSERT INTO `user1` VALUES ('2012-01-17', '41557', '474109', '3314', '5245');
INSERT INTO `user1` VALUES ('2012-01-18', '42679', '474237', '3338', '5351');
INSERT INTO `user1` VALUES ('2012-01-19', '43069', '475958', '3557', '5051');
INSERT INTO `user1` VALUES ('2012-01-20', '43933', '477310', '3527', '5188');
INSERT INTO `user1` VALUES ('2012-01-21', '44367', '477783', '3332', '5144');
INSERT INTO `user1` VALUES ('2012-01-22', '43402', '492308', '3662', '5438');
INSERT INTO `user1` VALUES ('2012-01-23', '42067', '481177', '3496', '5197');
INSERT INTO `user1` VALUES ('2012-01-24', '40446', '419007', '3093', '4769');
INSERT INTO `user1` VALUES ('2012-01-25', '37318', '426307', '3128', '4859');
INSERT INTO `user1` VALUES ('2012-01-26', '37010', '427116', '3409', '4896');
INSERT INTO `user1` VALUES ('2012-01-27', '39158', '447717', '3446', '4968');
INSERT INTO `user1` VALUES ('2012-01-28', '39877', '469591', '3410', '5159');
INSERT INTO `user1` VALUES ('2012-01-29', '41209', '500561', '3766', '5502');
INSERT INTO `user1` VALUES ('2012-01-30', '41610', '501886', '3801', '5460');
INSERT INTO `user1` VALUES ('2012-01-31', '43547', '506946', '3621', '5531');
INSERT INTO `user1` VALUES ('2012-02-01', '44705', '512795', '3944', '5515');
INSERT INTO `user1` VALUES ('2012-02-02', '43140', '520539', '4105', '5611');
INSERT INTO `user1` VALUES ('2012-02-03', '43349', '514190', '4001', '5556');
INSERT INTO `user1` VALUES ('2012-02-04', '47316', '549428', '4340', '5894');
INSERT INTO `user1` VALUES ('2012-02-05', '49281', '570498', '4424', '6057');
INSERT INTO `user1` VALUES ('2012-02-06', '47088', '558169', '4159', '5824');
INSERT INTO `user1` VALUES ('2012-02-07', '44632', '531200', '4045', '5600');
INSERT INTO `user1` VALUES ('2012-02-08', '42477', '530249', '4066', '5347');
INSERT INTO `user1` VALUES ('2012-02-09', '42078', '531894', '4229', '5816');
INSERT INTO `user1` VALUES ('2012-02-10', '44010', '538525', '4206', '5693');
INSERT INTO `user1` VALUES ('2012-02-11', '49903', '583250', '4364', '6193');
INSERT INTO `user1` VALUES ('2012-02-12', '51998', '609201', '4789', '6473');
INSERT INTO `user1` VALUES ('2012-02-13', '44916', '550446', '4317', '5811');
INSERT INTO `user1` VALUES ('2012-02-14', '44692', '569440', '4388', '6030');
INSERT INTO `user1` VALUES ('2012-02-15', '44961', '572123', '4429', '5960');
INSERT INTO `user1` VALUES ('2012-02-16', '44304', '564720', '4331', '5765');
INSERT INTO `user1` VALUES ('2012-02-17', '47936', '572453', '4563', '6073');
INSERT INTO `user1` VALUES ('2012-02-18', '56724', '634914', '4888', '6782');
INSERT INTO `user1` VALUES ('2012-02-19', '57450', '647103', '5054', '6852');
INSERT INTO `user1` VALUES ('2012-02-20', '46575', '591213', '4556', '6250');
INSERT INTO `user1` VALUES ('2012-02-21', '47058', '595630', '4588', '6211');
INSERT INTO `user1` VALUES ('2012-02-22', '45948', '596245', '4827', '6183');
INSERT INTO `user1` VALUES ('2012-02-23', '46347', '593270', '4503', '6214');
INSERT INTO `user1` VALUES ('2012-02-24', '48028', '608525', '4832', '6557');
INSERT INTO `user1` VALUES ('2012-02-25', '62927', '678426', '5431', '7484');
INSERT INTO `user1` VALUES ('2012-02-26', '58489', '681424', '5580', '7268');
INSERT INTO `user1` VALUES ('2012-02-27', '46482', '600393', '4639', '6417');
INSERT INTO `user1` VALUES ('2012-02-28', '46536', '594946', '4638', '6249');
INSERT INTO `user1` VALUES ('2012-02-29', '47134', '605641', '4564', '6423');
INSERT INTO `user1` VALUES ('2014-07-28', '11', '22', '33', '44');
INSERT INTO `user1` VALUES ('2014-08-26', 'f11', '1', '1', '1');
INSERT INTO `user1` VALUES ('2014-08-05', 'fdsds', 'fd', 'fdsfds', 'dsffds');
