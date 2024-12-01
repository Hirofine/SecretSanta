-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: SecretSanta
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `UserCadeau`
--

DROP TABLE IF EXISTS `UserCadeau`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserCadeau` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user1id` int DEFAULT NULL,
  `user2id` int DEFAULT NULL,
  `annee` int DEFAULT NULL,
  `user3id` int DEFAULT NULL,
  `user4id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_user1id` (`user1id`,`user2id`,`annee`),
  KEY `user2id` (`user2id`),
  KEY `user3id` (`user3id`),
  KEY `UserCadeau` (`user4id`),
  CONSTRAINT `UserCadeau_ibfk_1` FOREIGN KEY (`user1id`) REFERENCES `Users` (`id`),
  CONSTRAINT `UserCadeau_ibfk_2` FOREIGN KEY (`user2id`) REFERENCES `Users` (`id`),
  CONSTRAINT `UserCadeau_ibfk_3` FOREIGN KEY (`user3id`) REFERENCES `Users` (`id`),
  CONSTRAINT `UserCadeau_ibfk_4` FOREIGN KEY (`user4id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=228 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserCadeau`
--

LOCK TABLES `UserCadeau` WRITE;
/*!40000 ALTER TABLE `UserCadeau` DISABLE KEYS */;
INSERT INTO `UserCadeau` VALUES (162,16,18,2023,NULL,NULL),(163,7,15,2023,NULL,NULL),(164,8,13,2023,NULL,NULL),(165,15,10,2023,NULL,NULL),(166,20,11,2023,NULL,NULL),(167,9,16,2023,NULL,NULL),(168,19,17,2023,NULL,NULL),(169,14,7,2023,NULL,NULL),(170,17,19,2023,NULL,NULL),(171,13,9,2023,NULL,NULL),(172,11,8,2023,NULL,NULL),(173,18,20,2023,NULL,NULL),(174,10,14,2023,NULL,NULL),(215,16,14,2024,10,19),(216,19,15,2024,7,8),(217,10,17,2024,19,13),(218,20,11,2024,17,14),(219,7,20,2024,11,18),(220,17,8,2024,13,11),(221,14,7,2024,15,17),(222,8,19,2024,20,9),(223,15,18,2024,16,10),(224,11,9,2024,18,15),(225,9,16,2024,14,20),(226,13,10,2024,8,7),(227,18,13,2024,9,16);
/*!40000 ALTER TABLE `UserCadeau` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserLien`
--

DROP TABLE IF EXISTS `UserLien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserLien` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user1id` int DEFAULT NULL,
  `user2id` int DEFAULT NULL,
  `typeLien` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user1id` (`user1id`,`user2id`),
  KEY `user2id` (`user2id`),
  CONSTRAINT `UserLien_ibfk_1` FOREIGN KEY (`user1id`) REFERENCES `Users` (`id`),
  CONSTRAINT `UserLien_ibfk_2` FOREIGN KEY (`user2id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserLien`
--

LOCK TABLES `UserLien` WRITE;
/*!40000 ALTER TABLE `UserLien` DISABLE KEYS */;
INSERT INTO `UserLien` VALUES (5,7,8,0),(6,7,9,0),(7,8,9,0),(8,7,10,0),(9,10,11,0),(10,10,14,0),(11,11,14,0),(12,13,14,0),(13,15,16,0);
/*!40000 ALTER TABLE `UserLien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pseudo` varchar(255) NOT NULL,
  `passw` varchar(255) NOT NULL,
  `token` varchar(255) DEFAULT NULL,
  `tokenExpi` datetime DEFAULT NULL,
  `tokenSalt` varchar(255) DEFAULT NULL,
  `participate2024` tinyint(1) DEFAULT NULL,
  `participate2025` tinyint(1) DEFAULT NULL,
  `participate2023` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (7,'Apolline','$2b$12$86DMKb.PQ2aXUdt9TO7r3ewKrEaxsIKlx3AbGlwKokQ2njkB2JtbG','$2b$12$.GUAc4DkoqeuAax0U38FneMfta80yUiip1fUeZMCm7Nw0TpCASjCW','2023-12-09 05:25:30','$2b$12$AVrhYLw5TgoYLh25VVNm0u',1,NULL,1),(8,'Amélien','$2b$12$fPxb2OTY42s51VN2jCVGjuM5Z9kz1tuxrJVAdmjUDoOc7rK73dlsa','$2b$12$h1ii/yLg42lu3YwcF.qAVevAW4GkQt0QG3TLFdOs5PDJsPlVtA8zC','2023-12-15 04:44:22','$2b$12$afq40Z1qfhYltQ9crWGDSu',1,NULL,1),(9,'Théophane','$2b$12$JZQdmVwv8Xi.dPLmG9J7y.YbDW6t53XCALnu0RbCIyEOcaaM8ruVu','$2b$12$vL9bO5VRa/9CzptN0SCRpe/.6sCVZrLwIrRn5bwZ34wN7T7vqjH9G','2023-12-09 03:36:18','$2b$12$aaZ3iGxKD.gYZaXlduoGg.',1,NULL,1),(10,'Nathan','$2b$12$DyX65hLXK/vlTic8bwH1PuyWD/BSeTO/kUwyQqaNvwN8ysjJdYZFu','$2b$12$AR/TsIpANnXQ8vaNcegjnuNm8WPWSao8io/D3u0xNwowBjnetNV/u','2023-12-09 03:15:44','$2b$12$62RSiyGU5cE0Y49Zp/UOZe',1,NULL,1),(11,'Pénélope','$2b$12$cR7U9.B2oOeBama5oISOoOZGffxeud6jSU0GHbFMIF5AjgRsK6Dgy','$2b$12$CnxgynByjIVbxCwRvoX5VuQWsOfa/Bij0k.x2KDs49gTQ1sLLixuG','2023-12-09 03:25:57','$2b$12$cey0fcFruXnGfepGh4YL5u',1,NULL,1),(13,'Nicolas','$2b$12$yZbcdHxl2nclYUd/WWbx/u606thGj7KlDszRAz2uQhQYJ3YM8Eleq','$2b$12$J2K5Yp4tbdd04rkthF2tXu.xdIRyQh/4W1BFKzuncbo48nf0ovpau','2023-12-09 09:24:27','$2b$12$ecyM5SAPGXbwmN9jDTDCdu',1,NULL,1),(14,'Joséphine','$2b$12$pzCMMWptkDsBjfd.8aDnTuuL/kn9iSB/qxdWV1sbNxqDsdmWISROm','$2b$12$7470RUkcmP8BAwb0XPQiTeFZEy2vB0L996IjH6GBWStFo4z8SAcH.','2023-12-09 03:41:50','$2b$12$jOE.H3m6Cz9jJnUmFS560u',1,NULL,1),(15,'Pauline','$2b$12$OJhuptrjpptYlSOoCoKm5ur9gZle3uWTCf4QIn2EYL3nTpv42Ywhy','$2b$12$dkHGyzHyflua1hQUfnUBE.lfGy9II12GXnDl0exLdIaon35sZXgXO','2023-12-09 03:07:03','$2b$12$/Et96jetysFZ7uaW6IMKDe',1,NULL,1),(16,'Romain','$2b$12$oLK0rbKKLTz/cxcgwKtqK.aX6EViYM8ojf.JowLNE/Btts88I7nQy','$2b$12$bpLLSuaZgkHmJ7WBoFzGKeiV32HdTxvRrWgZWL40uE6gSLF1Ee1lq','2024-11-15 02:11:17','$2b$12$NSpaU0gocGG3j8DTdc9LCO',NULL,NULL,NULL),(17,'Rémy','$2b$12$CqYkxhUG5l/ALmHTLrKmdur2OV7EuWMr.qGmG1kvwLAFGQ4zT4QOu','$2b$12$YzNAdMtsWZJszHQI/vRLCOlxkRH542vg6DqaKoI.G6vKKYIoElcSq','2023-12-09 03:19:05','$2b$12$MMPQVe5ejqpPYJr1Ob3h5e',1,NULL,1),(18,'Jonas','$2b$12$3vEChIrOSrTl8y2ZzMT6n.w6MJT52uNUMAGZafsnBDpl55a6G8.jq','$2b$12$Jh3TmI.cOQg/Oa81WVMjv.q0K28nt2CLzTWntIS8q38y5n8ipaBnq','2023-12-09 03:40:35','$2b$12$8lw2.DioDeI5.gYhJrK6Pu',1,NULL,1),(19,'Alexi','$2b$12$lL0lLtL5CPLsTJa0JrN5Q.NK.MAPTESmHal/ZhcOpc7DzViItKWgG','$2b$12$JYNSmDkSDY7zFgK8DNk9d.pNydVG/X0Ep93zCbn/382gEOwWpr862','2023-12-09 03:09:44','$2b$12$ogeakSws.8JSKFO1ypFO.u',1,NULL,1),(20,'Gaby','$2b$12$nOOgf7h3tJkzmZgAgT0t0OgiE/Kr0wTDAOMI2Y/ltJvWymL01e2/W','$2b$12$DgtVTt3EW78uPPgj1pQ/Be6bml8NteM8Y/PJ89Jco6RS4oVPNgElm','2023-12-09 05:32:24','$2b$12$zjdnxBj7g4juXhC6TugVa.',1,NULL,1);
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-30 19:23:38
