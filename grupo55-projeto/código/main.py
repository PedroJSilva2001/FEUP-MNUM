from plots import plot_Dt
from data_processing import *
from math import exp, log

k_et = 0.17325   #kinetic total-elimination constant in per hour
t_max= 4.0  # instant in hours after administration when maximum plasma concentration occurs

def f(k_a):
    return k_a*exp(-k_a*t_max) - k_et*exp(-k_et*t_max)

def fder(k_a):
    return (-k_a**2)*t_max*exp(-k_a*t_max) + (k_et**2)*t_max * exp(-k_et*t_max)

def g2(k_a):
    return -log(  (k_et*exp(-k_et*t_max))/k_a )/t_max

def g(k_a):
    return k_et*exp((-k_et + k_a)*t_max )

k_a = 0.3466320541629992 # kinetic absorption constant in per hour

daily_dose = 150.0                 # in mg
half_dose = daily_dose/2.0         # in mg
days = 5.0                         #administrarion days
dt = 12.0                          #time between two pills in hours
time_offset = 0.5                  # reaction time in hours
t_up = t_max - time_offset         # time interval where D(t) grows
t_down = dt - t_max                # time interval where D(t) decreases
effective_time = dt - time_offset  # time interval where D(t) is not null
max_Dt = half_dose * 2.0/effective_time  # b value of y2 = m2*x+ b
Dt_slope1 = (max_Dt-0.0)/t_up                  # m1 value of y1 = m1 *x
Dt_slope2 =  (0.0 - max_Dt)/t_down  # m2 value of y2 = m2*x +b


# administration function
def D(t):
    if t >= days*dt*2:
        return 0
    while t >= dt:
        t -= dt
    if t <= time_offset :
        return 0
    if t <= t_max :
        return Dt_slope1*(t-time_offset)
    return Dt_slope2 * (t-t_max) + max_Dt

def mi_der(t, mi, mp):
    return D(t) - k_a*mi

def mp_der(t, mi, mp):
    return k_a*mi-k_et*mp

def main():
    plot_Dt(D, 24)
    tolerance = 1e-20
    a = 0.2
    b = 0.7
    x0 = 0.5
    ka_values, iterations, data = get_ka_results(tolerance, a, b, x0, f, fder, g2)
    errors = get_ka_errors(ka_values)
    #data[0].to_excel("NEWTON.xlsx", engine='xlsxwriter')
    #data[1].to_excel("BISSECAO.xlsx", engine='xlsxwriter')
    #data[2].to_excel("CORDA.xlsx", engine='xlsxwriter')
    #data[3].to_excel("CORDA_MOD.xlsx", engine='xlsxwriter')
    #data[4].to_excel("PICARD.xlsx", engine='xlsxwriter')
    #print_ka_results(ka_values, iterations, data, errors)
    t0 = 0
    mi0 = 0
    mp0 = 0
    tf = 7*24
    n = 200
    t1 = 0.84
    mi1 = 0.177391304347826
    mp1 = 0
    sister_cols_list, system_data_list = get_system_results(t0, mi0, mp0,t1, mi1, mp1,  tf, n, mi_der, mp_der)
    qc_list, qc_data_list = get_Qc_results(sister_cols_list)
    #system_data_list[0][0].to_excel("RK4_200.xlsx", engine='xlsxwriter')
    #system_data_list[0][1].to_excel("RK4_400.xlsx", engine='xlsxwriter')
    #system_data_list[0][2].to_excel("RK4_800.xlsx", engine='xlsxwriter')
    #system_data_list[1][0].to_excel("RK2_200.xlsx", engine='xlsxwriter')
    #system_data_list[1][1].to_excel("RK2_400.xlsx", engine='xlsxwriter')
    #system_data_list[1][2].to_excel("RK2_800.xlsx", engine='xlsxwriter')
    #system_data_list[2][0].to_excel("EULER_200.xlsx", engine='xlsxwriter')
    #system_data_list[2][1].to_excel("EULER_400.xlsx", engine='xlsxwriter')
    #system_data_list[2][2].to_excel("EULER_800.xlsx", engine='xlsxwriter')
    #system_data_list[3][0].to_excel("EULER_MOD_200.xlsx", engine='xlsxwriter')
    #system_data_list[3][1].to_excel("EULER_MOD_400.xlsx", engine='xlsxwriter')
    #system_data_list[3][2].to_excel("EULER_MOD_800.xlsx", engine='xlsxwriter')
    #print_system_results(system_data_list)
    #print_Qc_results(qc_data_list)
    #plot_results(sister_cols_list, qc_list)

if __name__ == "__main__":
    main()
