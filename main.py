from env import buildEnvironment
from sensors import LaserSensor
import pygame
environment=buildEnvironment((600,1200), "Test")
environment.originalMap = environment.map.copy()
laser=LaserSensor(200, environment.originalMap, uncertainty=(0.5,0.01))
environment.map.fill((0,0,0))
environment.infomap = environment.map.copy()

running = True

while running:
    sensorON=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if pygame.mouse.get_focused():
            sensorON=True
        elif not pygame.mouse.get_focused():
            sensorON=False
    if sensorON:
        position=pygame.mouse.get_pos()
        laser.position=position
        sensor_data = laser.sense_obstacles()
        environment.dataStorage(sensor_data)
        environment.show_sensorData()
    environment.map.blit(environment.infomap,(0,0))
    pygame.display.update()