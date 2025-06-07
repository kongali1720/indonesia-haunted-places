CREATE TABLE haunted_places (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  location VARCHAR(150) NOT NULL,
  description TEXT NOT NULL,
  history TEXT,
  reported_sightings TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
