-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 18, 2026 at 10:57 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1falldetectionreportdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Profile` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`, `Profile`) VALUES
(1, 'mark', '8148526949', 'fantasypythonprojects@gmail.com', 'Trichy', 'mark', 'mark', 'wp1816326-the-amazing-spider-man-wallpapers.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `reporttb`
--

CREATE TABLE `reporttb` (
  `id` bigint(50) NOT NULL auto_increment,
  `date` varchar(250) NOT NULL,
  `time` varchar(250) NOT NULL,
  `object_name` varchar(250) NOT NULL,
  `imgg` varchar(250) NOT NULL,
  `uname` varchar(250) NOT NULL,
  `profile` varchar(250) NOT NULL,
  `device` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `reporttb`
--

INSERT INTO `reporttb` (`id`, `date`, `time`, `object_name`, `imgg`, `uname`, `profile`, `device`) VALUES
(1, '2026-03-18', '16:23:14', 'Fall-Detected', 'static/assets/upload/1821.jpg', 'mark', 'wp1816326-the-amazing-spider-man-wallpapers.jpg', 'Logi C270 HD WebCam'),
(2, '2026-03-18', '16:23:20', 'Fall-Detected', 'static/assets/upload/6711.jpg', 'mark', 'wp1816326-the-amazing-spider-man-wallpapers.jpg', 'Logi C270 HD WebCam');
