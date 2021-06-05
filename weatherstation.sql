-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Mag 08, 2021 alle 16:09
-- Versione del server: 10.1.22-MariaDB
-- Versione PHP: 7.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `weatherstation`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `indoorweatherdata`
--

CREATE TABLE `indoorweatherdata` (
  `Date` datetime NOT NULL,
  `Temperature` float NOT NULL,
  `Humidity` float NOT NULL,
  `Pressure` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `indoorweatherdata`
--

INSERT INTO `indoorweatherdata` (`Date`, `Temperature`, `Humidity`, `Pressure`) VALUES
('2021-05-05 12:38:00', 26, 23, 3455),
('2021-05-05 12:39:00', 26.3, 23.7, 3455.8),
('2021-05-08 12:39:00', 26.3, 23.7, 3455.8),
('2021-05-05 13:11:00', 26.3, 23.7, 3455.8),
('2021-05-08 13:11:00', 26.3, 23.7, 3455.8),
('2021-05-08 13:11:00', 26.3, 23.7, 3455.8),
('2021-05-08 13:20:00', 26.3, 23.7, 3455.8),
('2021-05-08 13:20:00', 26.3, 23.7, 3455.8),
('2021-05-08 13:20:00', 26.3, 23.7, 3455.8),
('2021-05-08 13:22:00', 26.3, 23.7, 3455.8),
('2021-05-05 13:11:00', 26.3, 23.7, 3455.8);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
