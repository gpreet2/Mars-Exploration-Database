-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Mars Exploration DB
-- -----------------------------------------------------
DROP DATABASE IF EXISTS `MARS EXPLORATION DB`;
CREATE DATABASE IF NOT EXISTS `MARS EXPLORATION DB`;
USE `MARS EXPLORATION DB`;
-- -----------------------------------------------------
-- Table `user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `user` ;

CREATE TABLE IF NOT EXISTS `user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `date_joined` DATETIME NOT NULL,
  `last_login` DATETIME NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Mission`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mission` ;

CREATE TABLE IF NOT EXISTS `Mission` (
  `mission_id` INT NOT NULL AUTO_INCREMENT,
  `start_date` DATETIME NOT NULL,
  `end_date` DATETIME NOT NULL,
  `objective` VARCHAR(255) NOT NULL,
  `status` VARCHAR(50) NULL,
  PRIMARY KEY (`mission_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Rover`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Rover` ;

CREATE TABLE IF NOT EXISTS `Rover` (
  `rover_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `launch_date` DATETIME NOT NULL,
  `arrival_date` DATETIME NOT NULL,
  `status` VARCHAR(50) NOT NULL,
  `Mission_mission_id` INT NOT NULL,
  PRIMARY KEY (`rover_id`),
  INDEX `fk_Rover_Mission1_idx` (`Mission_mission_id` ASC) VISIBLE,
  CONSTRAINT `fk_Rover_Mission1`
    FOREIGN KEY (`Mission_mission_id`)
    REFERENCES `Mission` (`mission_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Visualization`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Visualization` ;

CREATE TABLE IF NOT EXISTS `Visualization` (
  `Visualization_id` INT NOT NULL AUTO_INCREMENT,
  `created_by` INT NOT NULL,
  PRIMARY KEY (`Visualization_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dataset`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Dataset` ;

CREATE TABLE IF NOT EXISTS `Dataset` (
  `dataset_id` INT NOT NULL AUTO_INCREMENT,
  `source_id` INT NOT NULL,
  `date_collected` VARCHAR(45) NOT NULL,
  `Mission_mission_id` INT NOT NULL,
  `Visualization_Visualization_id` INT NOT NULL,
  PRIMARY KEY (`dataset_id`),
  INDEX `fk_Dataset_Mission1_idx` (`Mission_mission_id` ASC) VISIBLE,
  INDEX `fk_Dataset_Visualization1_idx` (`Visualization_Visualization_id` ASC) VISIBLE,
  CONSTRAINT `fk_Dataset_Mission1`
    FOREIGN KEY (`Mission_mission_id`)
    REFERENCES `Mission` (`mission_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Dataset_Visualization1`
    FOREIGN KEY (`Visualization_Visualization_id`)
    REFERENCES `Visualization` (`Visualization_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Machine`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Machine` ;

CREATE TABLE IF NOT EXISTS `Machine` (
  `machine_id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(255) NOT NULL,
  `status` VARCHAR(255) NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  `Mission_mission_id` INT NOT NULL,
  PRIMARY KEY (`machine_id`),
  UNIQUE INDEX `machine_id_UNIQUE` (`machine_id` ASC) VISIBLE,
  INDEX `fk_Machine_Mission1_idx` (`Mission_mission_id` ASC) VISIBLE,
  CONSTRAINT `fk_Machine_Mission1`
    FOREIGN KEY (`Mission_mission_id`)
    REFERENCES `Mission` (`mission_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Components`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Components` ;

CREATE TABLE IF NOT EXISTS `Components` (
  `component_id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(255) NOT NULL,
  `status` VARCHAR(255) NOT NULL,
  `data_output` TEXT NOT NULL,
  `Machine_machine_id` INT NOT NULL,
  PRIMARY KEY (`component_id`),
  UNIQUE INDEX `component_id_UNIQUE` (`component_id` ASC) VISIBLE,
  INDEX `fk_Components_Machine1_idx` (`Machine_machine_id` ASC) VISIBLE,
  CONSTRAINT `fk_Components_Machine1`
    FOREIGN KEY (`Machine_machine_id`)
    REFERENCES `Machine` (`machine_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Research Team`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Research Team` ;

CREATE TABLE IF NOT EXISTS `Research Team` (
  `team_id` INT NOT NULL AUTO_INCREMENT,
  `team_name` VARCHAR(255) NOT NULL,
  `lead_researcher` INT NOT NULL,
  PRIMARY KEY (`team_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Discussion Thread`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Discussion Thread` ;

CREATE TABLE IF NOT EXISTS `Discussion Thread` (
  `Thread_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `created_by` INT NOT NULL,
  `created_date` DATE NOT NULL,
  `user_user_id` INT NOT NULL,
  PRIMARY KEY (`Thread_id`),
  INDEX `fk_Discussion Thread_user1_idx` (`user_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Discussion Thread_user1`
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Mars`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mars` ;

CREATE TABLE IF NOT EXISTS `Mars` (
  `mars_id` INT NOT NULL AUTO_INCREMENT,
  `region` VARCHAR(255) NOT NULL,
  `atmosphere_composition` TEXT NOT NULL,
  `surface_conditions` TEXT NOT NULL,
  `Marscol` VARCHAR(45) NULL,
  `Mission_mission_id` INT NOT NULL,
  PRIMARY KEY (`mars_id`),
  UNIQUE INDEX `mars_id_UNIQUE` (`mars_id` ASC) VISIBLE,
  INDEX `fk_Mars_Mission_idx` (`Mission_mission_id` ASC) VISIBLE,
  CONSTRAINT `fk_Mars_Mission`
    FOREIGN KEY (`Mission_mission_id`)
    REFERENCES `Mission` (`mission_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Martian Terrain`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Martian Terrain` ;

CREATE TABLE IF NOT EXISTS `Martian Terrain` (
  `terrain_id` INT NOT NULL AUTO_INCREMENT,
  `mineral_composition` TEXT NOT NULL,
  `characteristics` TEXT NOT NULL,
  `Mars_mars_id` INT NOT NULL,
  PRIMARY KEY (`terrain_id`),
  UNIQUE INDEX `terrain_id_UNIQUE` (`terrain_id` ASC) VISIBLE,
  INDEX `fk_Martian Terrain_Mars1_idx` (`Mars_mars_id` ASC) VISIBLE,
  CONSTRAINT `fk_Martian Terrain_Mars1`
    FOREIGN KEY (`Mars_mars_id`)
    REFERENCES `Mars` (`mars_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Research Document`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Research Document` ;

CREATE TABLE IF NOT EXISTS `Research Document` (
  `document_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `author_id` INT NOT NULL,
  `publish_date` DATE NOT NULL,
  `Research Team_team_id` INT NOT NULL,
  PRIMARY KEY (`document_id`),
  INDEX `fk_Research Document_Research Team1_idx` (`Research Team_team_id` ASC) VISIBLE,
  CONSTRAINT `fk_Research Document_Research Team1`
    FOREIGN KEY (`Research Team_team_id`)
    REFERENCES `Research Team` (`team_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Training Module`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Training Module` ;

CREATE TABLE IF NOT EXISTS `Training Module` (
  `module_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `length` INT NOT NULL,
  `difficulty_level` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`module_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Notification System`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Notification System` ;

CREATE TABLE IF NOT EXISTS `Notification System` (
  `notification_id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(100) NULL,
  `message` MEDIUMTEXT NOT NULL,
  `date_sent` DATETIME NOT NULL,
  `user_user_id` INT NOT NULL,
  PRIMARY KEY (`notification_id`),
  INDEX `fk_Notification System_user1_idx` (`user_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Notification System_user1`
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `API Access`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `API Access` ;

CREATE TABLE IF NOT EXISTS `API Access` (
  `apikey_id` INT NOT NULL AUTO_INCREMENT,
  `access_level` VARCHAR(100) NOT NULL,
  `issue_date` DATETIME NOT NULL,
  `expiry_date` DATETIME NOT NULL,
  `user_user_id` INT NOT NULL,
  PRIMARY KEY (`apikey_id`),
  INDEX `fk_API Access_user1_idx` (`user_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_API Access_user1`
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Role`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Role` ;

CREATE TABLE IF NOT EXISTS `Role` (
  `role_id` INT NOT NULL AUTO_INCREMENT,
  `role_name` VARCHAR(255) NOT NULL,
  `permissions` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`role_id`),
  UNIQUE INDEX `role_name_UNIQUE` (`role_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Account`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Account` ;

CREATE TABLE IF NOT EXISTS `Account` (
  `account_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `created_date` DATE NOT NULL,
  `last_activity_date` DATETIME NOT NULL,
  PRIMARY KEY (`account_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Saved Searches`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Saved Searches` ;

CREATE TABLE IF NOT EXISTS `Saved Searches` (
  `search_id` INT NOT NULL AUTO_INCREMENT,
  `account_id` INT NOT NULL,
  `search_query` MEDIUMTEXT NOT NULL,
  `user_user_id` INT NOT NULL,
  PRIMARY KEY (`search_id`),
  INDEX `fk_Saved Searches_user1_idx` (`user_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Saved Searches_user1`
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Mission Sensors`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mission Sensors` ;

CREATE TABLE IF NOT EXISTS `Mission Sensors` (
  `mission_sensors_id` INT NOT NULL AUTO_INCREMENT,
  `sensor_id` INT NOT NULL,
  `satellite_id` INT NOT NULL,
  `Mission_mission_id` INT NOT NULL,
  `Machine_machine_id` INT NOT NULL,
  PRIMARY KEY (`mission_sensors_id`, `Machine_machine_id`),
  INDEX `fk_Mission Sensors_Mission1_idx` (`Mission_mission_id` ASC) VISIBLE,
  INDEX `fk_Mission Sensors_Machine1_idx` (`Machine_machine_id` ASC) VISIBLE,
  CONSTRAINT `fk_Mission Sensors_Mission1`
    FOREIGN KEY (`Mission_mission_id`)
    REFERENCES `Mission` (`mission_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Mission Sensors_Machine1`
    FOREIGN KEY (`Machine_machine_id`)
    REFERENCES `Machine` (`machine_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Discussion Replies`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Discussion Replies` ;

CREATE TABLE IF NOT EXISTS `Discussion Replies` (
  `reply_id` INT NOT NULL AUTO_INCREMENT,
  `thread_id` INT NOT NULL,
  `reply_text` MEDIUMTEXT NOT NULL,
  `reply_date` DATETIME NOT NULL,
  `user_user_id` INT NOT NULL,
  `Discussion Thread_Thread_id` INT NOT NULL,
  PRIMARY KEY (`reply_id`),
  INDEX `fk_Discussion Replies_user1_idx` (`user_user_id` ASC) VISIBLE,
  INDEX `fk_Discussion Replies_Discussion Thread1_idx` (`Discussion Thread_Thread_id` ASC) VISIBLE,
  CONSTRAINT `fk_Discussion Replies_user1`
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Discussion Replies_Discussion Thread1`
    FOREIGN KEY (`Discussion Thread_Thread_id`)
    REFERENCES `Discussion Thread` (`Thread_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Document Citations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Document Citations` ;

CREATE TABLE IF NOT EXISTS `Document Citations` (
  `citation_id` INT NOT NULL AUTO_INCREMENT,
  `document_id` INT NOT NULL,
  `citation_text` MEDIUMTEXT NOT NULL,
  `Research Document_document_id` INT NOT NULL,
  PRIMARY KEY (`citation_id`, `Research Document_document_id`),
  INDEX `fk_Document Citations_Research Document1_idx` (`Research Document_document_id` ASC) VISIBLE,
  CONSTRAINT `fk_Document Citations_Research Document1`
    FOREIGN KEY (`Research Document_document_id`)
    REFERENCES `Research Document` (`document_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Module Feedback`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Module Feedback` ;

CREATE TABLE IF NOT EXISTS `Module Feedback` (
  `feedback_id` INT NOT NULL AUTO_INCREMENT,
  `module_id` INT NOT NULL,
  `rating` INT NOT NULL,
  `comment` MEDIUMTEXT NOT NULL,
  `user_user_id` INT NOT NULL,
  PRIMARY KEY (`feedback_id`),
  INDEX `fk_Module Feedback_user1_idx` (`user_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Module Feedback_user1`
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Mailing List`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Mailing List` ;

CREATE TABLE IF NOT EXISTS `Mailing List` (
  `list_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`list_id`),
  UNIQUE INDEX `list_id_UNIQUE` (`list_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Payment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Payment` ;

CREATE TABLE IF NOT EXISTS `Payment` (
  `payment_id` INT NOT NULL AUTO_INCREMENT,
  `amount` DECIMAL(10,2) NOT NULL,
  `date` TIMESTAMP NOT NULL,
  `method` VARCHAR(255) NOT NULL,
  `user_user_id` INT NOT NULL,
  `Account_account_id` INT NOT NULL,
  PRIMARY KEY (`payment_id`),
  UNIQUE INDEX `payment_id_UNIQUE` (`payment_id` ASC) VISIBLE,
  INDEX `fk_Payment_user1_idx` (`user_user_id` ASC) VISIBLE,
  INDEX `fk_Payment_Account1_idx` (`Account_account_id` ASC) VISIBLE,
  CONSTRAINT `fk_Payment_user1`
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Payment_Account1`
    FOREIGN KEY (`Account_account_id`)
    REFERENCES `Account` (`account_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Weather`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Weather` ;

CREATE TABLE IF NOT EXISTS `Weather` (
  `weather_id` INT NOT NULL AUTO_INCREMENT,
  `temperature` FLOAT NOT NULL,
  `pressure` FLOAT NOT NULL,
  `wind_speed` FLOAT NOT NULL,
  `Mission_mission_id` INT NOT NULL,
  PRIMARY KEY (`weather_id`),
  UNIQUE INDEX `weather_id_UNIQUE` (`weather_id` ASC) VISIBLE,
  INDEX `fk_Weather_Mission1_idx` (`Mission_mission_id` ASC) VISIBLE,
  CONSTRAINT `fk_Weather_Mission1`
    FOREIGN KEY (`Mission_mission_id`)
    REFERENCES `Mission` (`mission_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_has_Mailing List`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `user_has_Mailing List` ;

CREATE TABLE IF NOT EXISTS `user_has_Mailing List` (
  `user_user_id` INT NOT NULL,
  `Mailing List_list_id` INT NOT NULL,
  PRIMARY KEY (`user_user_id`, `Mailing List_list_id`),
  INDEX `fk_user_has_Mailing List_Mailing List1_idx` (`Mailing List_list_id` ASC) VISIBLE,
  INDEX `fk_user_has_Mailing List_user1_idx` (`user_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_Mailing List_user1`
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_Mailing List_Mailing List1`
    FOREIGN KEY (`Mailing List_list_id`)
    REFERENCES `Mailing List` (`list_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Research Team_has_user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Research Team_has_user` ;

CREATE TABLE IF NOT EXISTS `Research Team_has_user` (
  `Research Team_team_id` INT NOT NULL,
  `user_user_id` INT NOT NULL,
  PRIMARY KEY (`Research Team_team_id`, `user_user_id`),
  INDEX `fk_Research Team_has_user_user1_idx` (`user_user_id` ASC) VISIBLE,
  INDEX `fk_Research Team_has_user_Research Team1_idx` (`Research Team_team_id` ASC) VISIBLE,
  CONSTRAINT `fk_Research Team_has_user_Research Team1`
    FOREIGN KEY (`Research Team_team_id`)
    REFERENCES `Research Team` (`team_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Research Team_has_user_user1`
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Martian Terrain_has_Mission`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Martian Terrain_has_Mission` ;

CREATE TABLE IF NOT EXISTS `Martian Terrain_has_Mission` (
  `Martian Terrain_terrain_id` INT NOT NULL,
  `Mission_mission_id` INT NOT NULL,
  PRIMARY KEY (`Martian Terrain_terrain_id`, `Mission_mission_id`),
  INDEX `fk_Martian Terrain_has_Mission_Mission1_idx` (`Mission_mission_id` ASC) VISIBLE,
  INDEX `fk_Martian Terrain_has_Mission_Martian Terrain1_idx` (`Martian Terrain_terrain_id` ASC) VISIBLE,
  CONSTRAINT `fk_Martian Terrain_has_Mission_Martian Terrain1`
    FOREIGN KEY (`Martian Terrain_terrain_id`)
    REFERENCES `Martian Terrain` (`terrain_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Martian Terrain_has_Mission_Mission1`
    FOREIGN KEY (`Mission_mission_id`)
    REFERENCES `Mission` (`mission_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Training Module_has_user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Training Module_has_user` ;

CREATE TABLE IF NOT EXISTS `Training Module_has_user` (
  `Training Module_module_id` INT NOT NULL,
  `user_user_id` INT NOT NULL,
  PRIMARY KEY (`Training Module_module_id`, `user_user_id`),
  INDEX `fk_Training Module_has_user_user1_idx` (`user_user_id` ASC) VISIBLE,
  INDEX `fk_Training Module_has_user_Training Module1_idx` (`Training Module_module_id` ASC) VISIBLE,
  CONSTRAINT `fk_Training Module_has_user_Training Module1`
    FOREIGN KEY (`Training Module_module_id`)
    REFERENCES `Training Module` (`module_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Training Module_has_user_user1`
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `user_has_Role`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `user_has_Role` ;

CREATE TABLE IF NOT EXISTS `user_has_Role` (
  `user_user_id` INT NOT NULL,
  `Role_role_id` INT NOT NULL,
  PRIMARY KEY (`user_user_id`, `Role_role_id`),
  INDEX `fk_user_has_Role_Role1_idx` (`Role_role_id` ASC) VISIBLE,
  INDEX `fk_user_has_Role_user1_idx` (`user_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_has_Role_user1`
    FOREIGN KEY (`user_user_id`)
    REFERENCES `user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_Role_Role1`
    FOREIGN KEY (`Role_role_id`)
    REFERENCES `Role` (`role_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Role_has_Account`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Role_has_Account` ;

CREATE TABLE IF NOT EXISTS `Role_has_Account` (
  `Role_role_id` INT NOT NULL,
  `Account_account_id` INT NOT NULL,
  PRIMARY KEY (`Role_role_id`, `Account_account_id`),
  INDEX `fk_Role_has_Account_Account1_idx` (`Account_account_id` ASC) VISIBLE,
  INDEX `fk_Role_has_Account_Role1_idx` (`Role_role_id` ASC) VISIBLE,
  CONSTRAINT `fk_Role_has_Account_Role1`
    FOREIGN KEY (`Role_role_id`)
    REFERENCES `Role` (`role_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Role_has_Account_Account1`
    FOREIGN KEY (`Account_account_id`)
    REFERENCES `Account` (`account_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
