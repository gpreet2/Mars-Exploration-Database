-- Insert statements for 'user' table
INSERT INTO `user` (`username`, `email`, `date_joined`, `last_login`) VALUES
('john_doe', 'john.doe@example.com', '2023-10-25 09:00:00', NULL),
('jane_smith', 'jane.smith@example.com', '2023-10-25 09:15:00', NULL),
('bob_jones', 'bob.jones@example.com', '2023-10-25 09:30:00', NULL);

-- Insert statements for 'Mission' table
INSERT INTO `Mission` (`start_date`, `end_date`, `objective`, `status`) VALUES
('2023-11-01 08:00:00', '2023-12-31 18:00:00', 'Exploration of Mars Surface', 'In Progress'),
('2024-01-15 10:00:00', '2024-02-28 16:00:00', 'Atmospheric Study', 'Planned'),
('2024-03-10 12:00:00', '2024-04-30 20:00:00', 'Geological Analysis', 'Planned');

-- Insert statements for 'Rover' table
INSERT INTO `Rover` (`name`, `launch_date`, `arrival_date`, `status`, `Mission_mission_id`) VALUES
('Rover 1', '2023-11-01 08:00:00', '2023-11-07 14:00:00', 'Operational', 1),
('Rover 2', '2024-01-15 10:00:00', '2023-11-07 10:00:00', 'Planned', 2),
('Rover 3', '2024-03-10 12:00:00', '2023-11-07 12:00:00', 'Planned', 3);

-- Insert statements for 'Visualization' table
INSERT INTO `Visualization` (`created_by`) VALUES
(1),
(2),
(3);

-- Insert statements for 'Dataset' table
INSERT INTO `Dataset` (`source_id`, `date_collected`, `Mission_mission_id`, `Visualization_Visualization_id`) VALUES
(1, '2023-11-05', 1, 1),
(2, '2024-02-20', 2, 2),
(3, '2024-04-15', 3, 3);

-- Insert statements for 'Machine' table
INSERT INTO `Machine` (`type`, `status`, `location`, `Mission_mission_id`) VALUES
('Rover Control Center', 'Active', 'Mars Base 1', 1),
('Weather Station', 'Active', 'Mars Base 2', 2),
('Drilling Machine', 'Inactive', 'Mars Base 3', 3);

-- Insert statements for 'Components' table
INSERT INTO `Components` (`type`, `status`, `data_output`, `Machine_machine_id`) VALUES
('Control Panel', 'Operational', 'Control data output', 1),
('Sensor Module', 'Operational', 'Sensor data output', 2),
('Drill Head', 'Inactive', 'No data output', 3);

-- Insert statements for 'Research Team' table
INSERT INTO `Research Team` (`team_name`, `lead_researcher`) VALUES
('Exploration Team 1', 1),
('Science Team 2', 2),
('Research Team 3', 3);

-- Insert statements for 'Discussion Thread' table
INSERT INTO `Discussion Thread` (`title`, `created_by`, `created_date`, `user_user_id`) VALUES
('Mars Rocks Analysis', 1, '2023-11-02', 1),
('Atmospheric Data Discussion', 2, '2024-02-22', 2),
('Geological Findings', 3, '2024-04-17', 3);

-- Insert statements for 'Mars' table
INSERT INTO `Mars` (`region`, `atmosphere_composition`, `surface_conditions`, `Mission_mission_id`) VALUES
('Valles Marineris', 'CO2: 95%, N2: 3%, Ar: 1%', 'Rocky terrain', 1),
('Tharsis Planitia', 'CO2: 97%, N2: 2%, Ar: 0.5%', 'Desert-like', 2),
('Elysium Planitia', 'CO2: 96%, N2: 2.5%, Ar: 1%', 'Volcanic plains', 3);

-- Insert statements for 'Martian Terrain' table
INSERT INTO `Martian Terrain` (`mineral_composition`, `characteristics`, `Mars_mars_id`) VALUES
('Iron oxide, Silicates', 'Reddish, rocky', 1),
('Sulfur compounds, Basalt', 'Dusty, flat', 2),
('Volcanic rocks, Basalt', 'Cratered, uneven', 3);

-- Insert statements for 'Research Document' table
INSERT INTO `Research Document` (`document_id`,`title`, `author_id`, `publish_date`, `Research Team_team_id`) VALUES
(201,'Mars Surface Analysis', 1, '2023-11-10', 1),
(202,'Atmospheric Study Report', 2, '2024-02-28', 2),
(203,'Geological Findings Paper', 3, '2024-05-10', 3);

-- Insert statements for 'Training Module' table
INSERT INTO `Training Module` (`title`, `length`, `difficulty_level`) VALUES
('Introduction to Mars Exploration', 60, 'Beginner'),
('Atmospheric Data Collection', 45, 'Intermediate'),
('Geological Analysis Techniques', 75, 'Advanced');

-- Insert statements for 'Notification System' table
INSERT INTO `Notification System` (`type`, `message`, `date_sent`, `user_user_id`) VALUES
('Alert', 'Weather update: Dust storm detected', '2023-11-15 08:30:00', 1),
('Information', 'New dataset available for download', '2024-03-01 14:15:00', 2),
('Notification', 'Mission status update: In progress', '2024-05-05 10:00:00', 3);

-- Insert statements for 'API Access' table
INSERT INTO `API Access` (`access_level`, `issue_date`, `expiry_date`, `user_user_id`) VALUES
('Basic', '2023-10-25 09:00:00', '2024-10-25 09:00:00', 1),
('Standard', '2023-10-25 09:15:00', '2024-10-25 09:15:00', 2),
('Premium', '2023-10-25 09:30:00', '2024-10-25 09:30:00', 3);

-- Insert statements for 'Role' table
INSERT INTO `Role` (`role_name`, `permissions`) VALUES
('Administrator', 'Full access to all features'),
('Researcher', 'Access to research data and tools'),
('Guest', 'Limited access to public information');

INSERT INTO Account (account_id, user_id, created_date, last_activity_date)
VALUES 
(1, 1, '2023-10-25', '2023-10-25 10:00:00'),
(2, 2, '2023-10-24', '2023-10-25 11:00:00'),
(3, 3, '2023-10-23', '2023-10-25 12:00:00');

-- Insert statements for 'Role_has_Account' table
INSERT INTO Role_has_Account (`Role_role_id`, `Account_account_id`)
VALUES (1, 1), (2, 2), (3, 3);


-- Insert statements for 'Payment' table
INSERT INTO `Payment` (`amount`, `date`, `method`, `user_user_id`, `Account_account_id`) VALUES
(100.50, '2023-10-25 10:00:00', 'Credit Card', 1, 1),
(75.25, '2023-10-26 15:30:00', 'PayPal', 2, 2),
(120.00, '2023-10-27 12:45:00', 'Credit Card', 3, 3);

-- Insert statements for 'Weather' table
INSERT INTO `Weather` (`temperature`, `pressure`, `wind_speed`, `Mission_mission_id`) VALUES
(25.5, 1013.2, 15.0, 1),
(18.3, 1010.5, 12.5, 2),
(28.7, 1015.7, 20.2, 3);


INSERT INTO `Saved Searches` (search_id, account_id, search_query, user_user_id)
VALUES 
(1, 1, 'Mars exploration details', 1),
(2, 2, 'Latest research on Mars', 2),
(3, 3, 'Mars rover updates', 3);

INSERT INTO `Martian Terrain_has_Mission` (`Martian Terrain_terrain_id`, Mission_mission_id)
VALUES 
(1, 1),
(2, 2),
(3, 3);

INSERT INTO `Mission Sensors` (mission_sensors_id, sensor_id, satellite_id, Mission_mission_id, Machine_machine_id)
VALUES 
(1, 1, 1, 1, 1),
(2, 2, 2, 2, 2),
(3, 3, 3, 3, 3);


INSERT INTO `Discussion Replies` (reply_id, `thread_id`, `Discussion Thread_Thread_id`, reply_text, reply_date, user_user_id) 
VALUES 
(1, 1, 1, 'This is the first reply text.', '2023-10-25 10:00:00', 1), 
(2, 2, 2, 'This is the second reply text.', '2023-10-25 11:00:00', 2), 
(3, 3, 3, 'This is the third reply text.', '2023-10-25 12:00:00', 3);




INSERT INTO `Research Team_has_user` (`Research Team_team_id`, user_user_id)
VALUES 
(1, 1),
(1, 2),
(2, 3);


INSERT INTO `Training Module_has_user` (`Training Module_module_id`, user_user_id)
VALUES 
(1, 1),
(2, 1),
(2, 3);

INSERT INTO `user_has_Role` (user_user_id, Role_role_id)
VALUES 
(1, 1),
(2, 2),
(3, 3);


INSERT INTO `Module Feedback` (feedback_id, module_id, rating, comment, user_user_id)
VALUES 
(1, 1, 4, 'Very informative module.', 1),
(2, 2, 3, 'Decent content, could be improved.', 2),
(3, 1, 5, 'Great module! Learned a lot.', 3);

INSERT INTO `Mailing List` (list_id, name, description)
VALUES 
(1, 'Newsletter', 'Monthly newsletter updates.'),
(2, 'Promotions', 'Latest promotions and deals.'),
(3, 'Event Alerts', 'Updates about upcoming events.');

INSERT INTO `user_has_Mailing List` (user_user_id, `Mailing List_list_id`)
VALUES 
(1, 1),  -- User 1 has subscribed to the Newsletter
(1, 3),  -- User 1 has also subscribed to Event Alerts
(2, 2),  -- User 2 has subscribed to Promotions
(3, 1),  -- User 3 has subscribed to the Newsletter
(3, 2);  -- User 3 has also subscribed to Promotions

INSERT INTO `Document Citations` (citation_id, document_id, citation_text, `Research Document_document_id`) 
VALUES 
(1, 101, 'Doe, J. (2022). Importance of Research. Journal of Science.', 201), 
(2, 102, 'Smith, A. (2023). Innovative Methods. Engineering Digest.', 202), 
(3, 103, 'Lee, C. (2020). Sustainable Practices. Environment Weekly.', 203);









