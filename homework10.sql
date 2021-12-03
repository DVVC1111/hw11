-- -------------------------------------------------------------
-- TablePlus 4.5.0(396)
--
-- https://tableplus.com/
--
-- Database: homework10
-- Generation Time: 2021-12-03 15:44:12.4070
-- -------------------------------------------------------------


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


DROP TABLE IF EXISTS `coffee`;
CREATE TABLE `coffee` (
  `coffee_id` int(11) NOT NULL AUTO_INCREMENT,
  `coffee_name` text NOT NULL,
  `coffee_price` float NOT NULL,
  `mat_id` int(11) NOT NULL,
  PRIMARY KEY (`coffee_id`),
  KEY `mat_id` (`mat_id`),
  CONSTRAINT `coffee_ibfk_1` FOREIGN KEY (`mat_id`) REFERENCES `material` (`mat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `cus_id` int(11) NOT NULL AUTO_INCREMENT,
  `cus_firstname` text NOT NULL,
  `cus_lastname` text NOT NULL,
  `cus_ph` text NOT NULL,
  PRIMARY KEY (`cus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `material`;
CREATE TABLE `material` (
  `mat_id` int(11) NOT NULL AUTO_INCREMENT,
  `mat_water` float NOT NULL,
  `mat_cofbean` float NOT NULL,
  `mat_sugar` float NOT NULL,
  PRIMARY KEY (`mat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `resource`;
CREATE TABLE `resource` (
  `res_id` int(11) NOT NULL AUTO_INCREMENT,
  `water` float NOT NULL,
  `cof_bean` float NOT NULL,
  `sugar` float NOT NULL,
  PRIMARY KEY (`res_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `sell`;
CREATE TABLE `sell` (
  `sell_id` int(11) NOT NULL AUTO_INCREMENT,
  `cus_id` int(11) NOT NULL,
  `coffee_id` int(11) NOT NULL,
  `sell_total` float NOT NULL,
  `sell_date` date NOT NULL,
  PRIMARY KEY (`sell_id`),
  KEY `cus_id` (`cus_id`),
  KEY `coffee_id` (`coffee_id`),
  CONSTRAINT `sell_ibfk_1` FOREIGN KEY (`cus_id`) REFERENCES `customer` (`cus_id`),
  CONSTRAINT `sell_ibfk_2` FOREIGN KEY (`coffee_id`) REFERENCES `coffee` (`coffee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

INSERT INTO `coffee` (`coffee_id`, `coffee_name`, `coffee_price`, `mat_id`) VALUES
(1, 'Americano', 1.5, 1),
(2, 'Latte', 2, 2),
(3, 'Cappuccino', 2.5, 3);

INSERT INTO `customer` (`cus_id`, `cus_firstname`, `cus_lastname`, `cus_ph`) VALUES
(1, 'David', 'Vicheth', '012000111'),
(2, 'Steve ', 'Carrel', '012111000'),
(3, 'Lionel', 'Messi', '023000111'),
(4, 'Cristiano', 'Ronaldo', '023111000'),
(5, 'Joe', 'Chea', '088000111'),
(6, 'Jacky', 'Soun', '088111000'),
(7, 'Joe', 'Garner', '012909090'),
(8, 'David', 'Micheal', '012122111'),
(9, 'Tom', 'Dallis', '087820129'),
(10, 'Dave', 'Bautista', '01233111'),
(11, 'Raksa', 'Ma', '0121212120');

INSERT INTO `material` (`mat_id`, `mat_water`, `mat_cofbean`, `mat_sugar`) VALUES
(1, 15, 20, 5),
(2, 30, 10, 20),
(3, 10, 22, 10);

INSERT INTO `resource` (`res_id`, `water`, `cof_bean`, `sugar`) VALUES
(1, 970, 6410, 235);

INSERT INTO `sell` (`sell_id`, `cus_id`, `coffee_id`, `sell_total`, `sell_date`) VALUES
(10, 1, 1, 1, '2021-10-15'),
(11, 2, 2, 1, '2021-10-18'),
(12, 3, 3, 1, '2021-10-26'),
(13, 4, 3, 1, '2021-11-11'),
(14, 5, 1, 1, '2021-11-19'),
(15, 6, 2, 1, '2021-12-01'),
(16, 7, 2, 1, '2021-12-03'),
(17, 10, 1, 1, '2021-12-03'),
(18, 10, 1, 1, '2021-12-03'),
(19, 10, 1, 1, '2021-12-03'),
(20, 10, 1, 1, '2021-12-03'),
(21, 10, 1, 1, '2021-12-03'),
(22, 10, 1, 1, '2021-12-03'),
(23, 2, 2, 1, '2021-12-03'),
(24, 9, 3, 1, '2021-12-03'),
(25, 9, 2, 1, '2021-12-03'),
(26, 9, 1, 1, '2021-12-03'),
(27, 9, 2, 1, '2021-12-03'),
(28, 4, 1, 1, '2021-12-03'),
(29, 4, 2, 1, '2021-12-03');



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;