import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# กำหนดตัวแปร Input
velocity = ctrl.Antecedent(np.arange(0, 101, 1), 'Velocity')
steering_angle = ctrl.Antecedent(np.arange(-90, 91, 1), 'Steering Angle')

# กำหนดชั้นของตัวแปร Input
velocity['Slow'] = fuzz.trimf(velocity.universe, [0, 0, 40])
velocity['Moderate'] = fuzz.trimf(velocity.universe, [30, 50, 70])
velocity['Fast'] = fuzz.trimf(velocity.universe, [60, 100, 100])

steering_angle['Sharp'] = fuzz.trimf(steering_angle.universe, [-90, -60, -30])
steering_angle['Medium'] = fuzz.trimf(steering_angle.universe, [-45, 0, 45])
steering_angle['Gentle'] = fuzz.trimf(steering_angle.universe, [30, 60, 90])

# กำหนดตัวแปร Output
speed = ctrl.Consequent(np.arange(0, 101, 1), 'Speed')

# กำหนดชั้นของตัวแปร Output
speed['Slow'] = fuzz.trimf(speed.universe, [0, 0, 40])
speed['Fast'] = fuzz.trimf(speed.universe, [30, 50, 70])

# กำหนดกฎ Fuzzy Logic
rule1 = ctrl.Rule(velocity['Slow'] & steering_angle['Sharp'], speed['Slow'])
rule2 = ctrl.Rule(velocity['Fast'] & steering_angle['Gentle'], speed['Fast'])

# สร้างระบบ Fuzzy Logic
speed_ctrl = ctrl.ControlSystem([rule1, rule2])
speed_simulation = ctrl.ControlSystemSimulation(speed_ctrl)

# กำหนดค่า Input
speed_simulation.input['Velocity'] = 20
speed_simulation.input['Steering Angle'] = -45

# คำนวณค่า Output
speed_simulation.compute()

# แสดงผลลัพธ์
print("Estimated Speed:", speed_simulation.output['Speed'])
