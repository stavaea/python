/*
Navicat MySQL Data Transfer

Source Server         : dev
Source Server Version : 50722
Source Host           : 192.168.10.43:3306
Source Database       : db_course_log

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-04-23 10:31:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_stat_class
-- ----------------------------
DROP TABLE IF EXISTS `t_stat_class`;
CREATE TABLE `t_stat_class` (
  `pkid` int(11) NOT NULL AUTO_INCREMENT,
  `plan_id` int(11) NOT NULL,
  `start_stop` enum('start','stop') NOT NULL,
  `t` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `inserttime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`pkid`),
  KEY `plan_id` (`plan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1537 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_stat_good
-- ----------------------------
DROP TABLE IF EXISTS `t_stat_good`;
CREATE TABLE `t_stat_good` (
  `pkid` int(11) NOT NULL AUTO_INCREMENT,
  `plan_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `num` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`pkid`),
  UNIQUE KEY `plan_id` (`plan_id`,`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6167 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_stat_online
-- ----------------------------
DROP TABLE IF EXISTS `t_stat_online`;
CREATE TABLE `t_stat_online` (
  `pkid` int(11) NOT NULL AUTO_INCREMENT,
  `plan_id` int(11) NOT NULL,
  `t` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `num` int(11) NOT NULL,
  `content` text NOT NULL,
  PRIMARY KEY (`pkid`),
  KEY `plan_id` (`plan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5072 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_stat_signal
-- ----------------------------
DROP TABLE IF EXISTS `t_stat_signal`;
CREATE TABLE `t_stat_signal` (
  `pkid` int(11) NOT NULL AUTO_INCREMENT,
  `plan_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `stat_item` enum('agree','ask') NOT NULL DEFAULT 'agree' COMMENT 'ask:举手，agree：发言',
  `num` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`pkid`),
  UNIQUE KEY `plan_id` (`plan_id`,`user_id`,`stat_item`)
) ENGINE=InnoDB AUTO_INCREMENT=1386 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_stat_signal_plan
-- ----------------------------
DROP TABLE IF EXISTS `t_stat_signal_plan`;
CREATE TABLE `t_stat_signal_plan` (
  `pkid` int(11) NOT NULL AUTO_INCREMENT,
  `plan_id` int(11) NOT NULL,
  `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ss` int(11) NOT NULL,
  PRIMARY KEY (`pkid`),
  UNIQUE KEY `plan_id` (`plan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=697 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_stat_text
-- ----------------------------
DROP TABLE IF EXISTS `t_stat_text`;
CREATE TABLE `t_stat_text` (
  `pkid` int(11) NOT NULL AUTO_INCREMENT,
  `plan_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `num` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`pkid`),
  UNIQUE KEY `plan_id` (`plan_id`,`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6431 DEFAULT CHARSET=utf8;
