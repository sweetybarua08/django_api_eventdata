-- Set SQL_MODE and other settings if needed
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Create the match_info table
CREATE TABLE match_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    liveStatus VARCHAR(70),
    matchId INT(11),
    teamName VARCHAR(255),
    oversActual FLOAT(20),
    isFour BOOLEAN,
    isSix BOOLEAN,
    isWicket BOOLEAN,
    lastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL
);
