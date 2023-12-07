-- CREATE TABLE SecretSanta (
   -- id INT AUTO_INCREMENT PRIMARY KEY,
   -- annee INT,
   -- groupe VARCHAR(255)
-- );

-- Table Users
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pseudo VARCHAR(255) NOT NULL,
    passw VARCHAR(255) NOT NULL,
    token VARCHAR(255),
    tokenExpi DATETIME,
    tokenSalt VARCHAR(255)
);

-- Table UserCadeau
CREATE TABLE UserCadeau(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user1id INT,
    user2id INT,
    annee INT,
    UNIQUE (user1id, user2id),
    FOREIGN KEY (user1id) REFERENCES Users(id),
    FOREIGN KEY (user2id) REFERENCES Users(id)
);

-- Table UserLien
CREATE TABLE UserLien(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user1id INT,
    user2id INT,
    typeLien INT,
    UNIQUE (user1id, user2id),
    FOREIGN KEY (user1id) REFERENCES Users(id),
    FOREIGN KEY (user2id) REFERENCES Users(id)
);