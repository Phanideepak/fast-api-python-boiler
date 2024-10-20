create database ems;

use ems;

CREATE TABLE ems.users(
    `id` int NOT NULL AUTO_INCREMENT,
    `firstname` varchar(255) NOT NULL,
    `lastname` varchar(255) NOT NULL,
    `email` varchar(255) NOT NULL UNIQUE,
    `password` varchar(255) NOT NULL,
    `role` ENUM('ROLE_ADMIN','ROLE_HR','ROLE_FINANCE','ROLE_EMPLOYEE') default 'ROLE_ADMIN' not null,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
     PRIMARY KEY (`id`)
);

CREATE TABLE ems.department (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `is_approved` tinyint(1) NOT NULL DEFAULT '0',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  `approved_by` int,
  `approved_at` timestamp NULL,
  `deleted_by` int,
  `deleted_at` timestamp NULL,
  `created_by` int NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `description` (`description`)
);

CREATE TABLE ems.address(
    `id` int NOT NULL AUTO_INCREMENT,
    `first_line` varchar(255) NOT NULL,
    `second_line` varchar(255) NULL,
    `land_mark` varchar(255) NULL,
    `phone` varchar(20) NOT NULL,
    `city` varchar(100) NOT NULL,
    `pincode` varchar(20) NOT NULL,
    `state` VARCHAR(20) NOT NULL,
    `is_primary`  tinyint(1) NOT NULL DEFAULT '1',
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
     PRIMARY KEY (`id`),
     CONSTRAINT UC_FIRST_SECOND_CITY UNIQUE(`first_line`, `second_line`, `city`) 
);

CREATE TABLE ems.employee (
  `id` int NOT NULL AUTO_INCREMENT,
   `eid` varchar(20) NOT NULL UNIQUE, 
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `is_approved` tinyint(1) NOT NULL DEFAULT '0',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  `approved_by` int,
  `approved_at` timestamp NULL,
  `deleted_by` int,
  `deleted_at` timestamp NULL,
  `dept_id` int NOT NULL,
  `address_id` int NULL,
  `created_by` int NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`dept_id`) REFERENCES ems.department(id),
  FOREIGN KEY(`address_id`) REFERENCES ems.address(id)
);