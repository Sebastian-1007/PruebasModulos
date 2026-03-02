/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.32-MariaDB : Database - sistema_aspirantes
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`sistema_aspirantes` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `sistema_aspirantes`;

/*Table structure for table `aspirantes` */

DROP TABLE IF EXISTS `aspirantes`;

CREATE TABLE `aspirantes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `consecutivo` int(11) DEFAULT NULL,
  `folio` varchar(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `paterno` varchar(100) NOT NULL,
  `materno` varchar(100) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `sexo` varchar(20) NOT NULL,
  `programa` varchar(200) NOT NULL,
  `curp` varchar(20) NOT NULL,
  `foto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `consecutivo` (`consecutivo`),
  KEY `consecutivo_2` (`consecutivo`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `aspirantes` */

LOCK TABLES `aspirantes` WRITE;

insert  into `aspirantes`(`id`,`consecutivo`,`folio`,`nombre`,`paterno`,`materno`,`fecha_nacimiento`,`sexo`,`programa`,`curp`,`foto`) values (1,1000,'','SEBASTIAN','ROJAS','NUNEZ','2005-08-09','Masculino','Licenciatura en Administración','RONS071005HJMXML0','static/fotos\\1000_foto.png'),(2,1001,'NR4966GG','ERNESTO','ROJAS','NUNEZ','2005-02-03','Masculino','Derecho','RONS071005HJMXML6','static/fotos\\1001_foto.png'),(3,1002,'XI1357BD','KARLA','ROJAS','NUNEZ','2008-09-07','Femenino','Ingeniería en Sistemas','RONS071005HJLLML0','static/fotos\\1002_foto.png'),(4,1003,'JB4493UE','CAMILO','MARTINEZ','SUARES','2002-07-08','Masculino','Ingeniería en Sistemas','RONN071005HJMXML0','static/fotos\\1003_foto.png'),(5,1004,'JS7493BJ','EDUARDO','MARTINEZ','PAVEL','2004-08-09','Masculino','Ingeniería en Sistemas','RPS071005HJMXML0PP','static/fotos\\1004_foto.png'),(6,1005,'RR0143PT','EDUARDO','MARTINEZ','PAVEL','2004-08-09','Masculino','Ingeniería en Sistemas','RPS071005HJMXML0PP','static/fotos\\1005_foto.png'),(7,1006,'LU7173DR','SEBASTIAN','ROJAS','NUNEZ','2008-09-07','Masculino','Ingeniería en Sistemas','RONS071005HJMXML0','static/fotos\\1006_foto.png');

UNLOCK TABLES;

/*Table structure for table `directivos` */

DROP TABLE IF EXISTS `directivos`;

CREATE TABLE `directivos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `paterno` varchar(100) NOT NULL,
  `materno` varchar(100) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `puesto` varchar(100) NOT NULL COMMENT 'Ej: Director, Subdirector, Jefe de Departamento',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `directivos` */

LOCK TABLES `directivos` WRITE;

insert  into `directivos`(`id`,`nombre`,`paterno`,`materno`,`telefono`,`puesto`,`created_at`) values (1,'Admin','Sistema','Root','555-000-0000','Administrador del Sistema','2026-03-01 15:27:48'),(2,'Administrador','Principal','del Sistema','555-000-0000','Administrador General','2026-03-01 15:40:25'),(3,'Admin','Sistema','Root','555-000-0000','Administrador del Sistema','2026-03-01 16:04:49'),(4,'Raul','ROJAS','Cruz','7226737491','Subdirector','2026-03-01 22:18:50'),(5,'CAMILO','MARTINEZ','PAVEL','7226737491','Jefe de Departamento','2026-03-02 02:42:28');

UNLOCK TABLES;

/*Table structure for table `docentes` */

DROP TABLE IF EXISTS `docentes`;

CREATE TABLE `docentes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `paterno` varchar(100) NOT NULL,
  `materno` varchar(100) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `grado_academico` varchar(100) NOT NULL COMMENT 'Ej: Licenciatura, Maestría, Doctorado',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `docentes` */

LOCK TABLES `docentes` WRITE;

insert  into `docentes`(`id`,`nombre`,`paterno`,`materno`,`telefono`,`grado_academico`,`created_at`) values (1,'KARLA','MARTINEZ','PAVEL','7226737400','Maestría','2026-03-01 22:22:18'),(2,'EDUARDO','MARTINEZ','SUARES','7226737491','Especialidad','2026-03-02 02:40:54');

UNLOCK TABLES;

/*Table structure for table `pagos` */

DROP TABLE IF EXISTS `pagos`;

CREATE TABLE `pagos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aspirante_id` int(11) NOT NULL,
  `referencia` varchar(50) NOT NULL,
  `monto` decimal(10,2) NOT NULL,
  `estatus` varchar(20) DEFAULT 'Pendiente',
  PRIMARY KEY (`id`),
  KEY `fk_pago_aspirante` (`aspirante_id`),
  CONSTRAINT `fk_pago_aspirante` FOREIGN KEY (`aspirante_id`) REFERENCES `aspirantes` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `pagos` */

LOCK TABLES `pagos` WRITE;

insert  into `pagos`(`id`,`aspirante_id`,`referencia`,`monto`,`estatus`) values (1,1,'BBVA20261000',500.00,'Pendiente'),(2,2,'BBVA20261001',500.00,'Pendiente'),(3,3,'BBVA20261002',500.00,'Pendiente'),(4,4,'BBVA20261003',500.00,'Pendiente'),(5,5,'BBVA20261004',500.00,'Pendiente'),(7,7,'BBVA20261006',500.00,'Pendiente');

UNLOCK TABLES;

/*Table structure for table `usuarios` */

DROP TABLE IF EXISTS `usuarios`;

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `correo` varchar(120) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `rol` enum('aspirante','docente','directivo') NOT NULL DEFAULT 'aspirante',
  `activo` tinyint(1) DEFAULT 1,
  `aspirante_id` int(11) DEFAULT NULL,
  `docente_id` int(11) DEFAULT NULL,
  `directivo_id` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `correo` (`correo`),
  KEY `fk_usuario_aspirante` (`aspirante_id`),
  KEY `fk_usuario_docente` (`docente_id`),
  KEY `fk_usuario_directivo` (`directivo_id`),
  CONSTRAINT `fk_usuario_aspirante` FOREIGN KEY (`aspirante_id`) REFERENCES `aspirantes` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_usuario_directivo` FOREIGN KEY (`directivo_id`) REFERENCES `directivos` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_usuario_docente` FOREIGN KEY (`docente_id`) REFERENCES `docentes` (`id`) ON DELETE CASCADE,
  CONSTRAINT `chk_unico_rol` CHECK (`aspirante_id` is not null and `docente_id` is null and `directivo_id` is null or `aspirante_id` is null and `docente_id` is not null and `directivo_id` is null or `aspirante_id` is null and `docente_id` is null and `directivo_id` is not null)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `usuarios` */

LOCK TABLES `usuarios` WRITE;

insert  into `usuarios`(`id`,`correo`,`password_hash`,`rol`,`activo`,`aspirante_id`,`docente_id`,`directivo_id`,`created_at`,`updated_at`) values (1,'saedsaroj@gmail.com','$2b$12$Um9IV7fZdjaHBhTA20lxhuX2LuWcvaBRXNHVSVqOhalTRuG65U.HW','aspirante',1,7,NULL,NULL,'2026-03-01 14:55:43','2026-03-01 14:55:43'),(3,'administrador@escuela.edu.mx','$2b$12$K8Z0gY7LR9nJk7L8q9Wq1eJk7L8q9Wq1eJk7L8q9Wq1eJk7L8q9Wq1','directivo',1,NULL,NULL,2,'2026-03-01 15:40:40','2026-03-01 15:40:40'),(4,'admin@escuela.edu.mx','$2b$12$xk39v2rDlM8tT22lq31be.oMmdZqkKQNR.g0wdRWIW1UnAWK7/NHG','directivo',1,NULL,NULL,1,'2026-03-01 16:04:54','2026-03-01 22:15:04'),(5,'raul.rojas@directivo.escuela.edu.mx','$2b$12$0Pq6OYg4xMUCMo0OnckFq.SfZu2q4PGkxgrAlb0cyNIk/WH8ohrny','directivo',1,NULL,NULL,4,'2026-03-01 22:18:50','2026-03-01 22:18:50'),(6,'karla.martinez@docente.escuela.edu.mx','$2b$12$dnDg5gA3sIlqoABfhJ9MYO5Xwn1PZ37fohaskmnrRjgHlwGXhuwSO','docente',1,NULL,1,NULL,'2026-03-01 22:22:18','2026-03-01 22:22:18'),(7,'eduardo.martinez@docente.escuela.edu.mx','$2b$12$zzkMTdPJQwn9hKYS4No5oeO3m1v2xRe/e4La0IUPQWOZoWSaYuqZq','docente',1,NULL,2,NULL,'2026-03-02 02:40:54','2026-03-02 02:40:54'),(8,'camilo.martinez@directivo.escuela.edu.mx','$2b$12$YfzkS2/ZBR3xft9aNJpO6uBKo1rVwCQxh9IJQCO6SKdLIyhkZ5NBu','directivo',1,NULL,NULL,5,'2026-03-02 02:42:28','2026-03-02 02:42:28');

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
