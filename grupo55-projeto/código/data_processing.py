from root_finding_algorithms import*
from differential_equations_algorithms import*
from plots import*
reference_value = 0.3466320541629992

def get_error(value):
    return reference_value - value, (reference_value - value)/reference_value

def get_Qc(m_values, m1_values, m2_values):
    m1 = [m1_values[i] for i in range(len(m1_values)) if i%2 == 0]
    m2 = [m2_values[i] for i in range(len(m2_values)) if i%4 == 0]
    qc = [(m1[i] - m_values[i])/(m2[i]-m1[i]) if m2[i]-m1[i] != 0 else 0 for i in range(len(m_values))]
    return qc

def get_ka_results(tolerance, a, b, x0, f, fder, g):
    print("Iteration tables for Ka: ")
    ka1, data1, n1 = newton(x0, f, fder, tolerance)
    ka2, data2, n2 = bissection(a, b, f, tolerance)
    ka3, data3, n3 = false_position(a, b, f, tolerance)
    ka4, data4, n4 = modified_false_position(a, b, f, tolerance)
    ka5, data5, n5 = picard_peano(x0, f, g, tolerance)
    ka_values = [ka1, ka2, ka3, ka4, ka5]
    iterations = [n1, n2, n3, n4, n5]
    data = [data1, data2, data3, data4, data5]
    return ka_values, iterations, data

def get_ka_errors(ka_values):
    errors = []
    for i in range(len(ka_values)):
        abs_error, rel_error = get_error(ka_values[i])
        errors.append([abs_error, rel_error])
    return errors

def print_ka_results(ka_values, iterations, data, errors):
    methods = ["Newton", "Bissection", "False Position", "False Position modified", "Picard-Peano"]
    print("\n***********************************\nIteration tables for Ka\n***********************************")
    for i in range(len(methods)):
        print("\n___________________________________\n"+ methods[i] + ":")
        print(data[i])
    for i in range(len(methods)):
        method = methods[i]
        ka = ka_values[i]
        it = iterations[i]
        abs_error = errors[i][0]
        rel_error = errors[i][1]
        print("\n{}\n      iterations = {} \n      root = {} \n      absolute error = {} \n      relative error = {}".format(method, it, ka, abs_error, rel_error))

def get_system_results(t0, mi0, mp0,t1, mi1, mp1,  tf, n, mi_der, mp_der):
    sister_cols_rk4, data_rk4 = runge_kutta4_higher_order(t0, mi0, mp0, tf, n, mi_der, mp_der)
    sister_cols_rk2, data_rk2 = runge_kutta2_higher_order(t0, mi0, mp0, tf, n, mi_der, mp_der)
    sister_cols_euler, data_euler = euler_higher_order(t0, mi0, mp0, tf, n, mi_der, mp_der)
    sister_cols_mod_euler, data_mod_euler = modified_euler_higher_order(t0, mi0, mp0, t1,mi1, mp1, tf, n, mi_der, mp_der)
    sister_cols_list = [sister_cols_rk4, sister_cols_rk2, sister_cols_euler, sister_cols_mod_euler]
    data_list = [data_rk4, data_rk2, data_euler, data_mod_euler]
    return sister_cols_list, data_list

def print_system_results(data_list):
    methods = ["Runge Kutta 4", "Runge Kutta 2", "Euler", "Euler modified"]
    print("\n\n\n***********************************\nIteration tables for t, mi , mp\n***********************************")
    for i in range(len(methods)):
        print("\n___________________________________\n"+ methods[i] + ":")
        data = data_list[i]
        for table in data:
            print(table)

def get_Qc_results(sister_cols_list):
    qc_list = []
    data_list = []
    for sister_cols in sister_cols_list:
        mi = sister_cols[0]["y"]
        mi1 = sister_cols[1]["y"]
        mi2 = sister_cols[2]["y"]
        mp = sister_cols[0]["z"]
        mp1 = sister_cols[1]["z"]
        mp2 = sister_cols[2]["z"]
        qc_mi = get_Qc(mi, mi1, mi2)
        qc_mp = get_Qc(mp, mp1, mp2)
        qc_list.append([qc_mi, qc_mp])
        data_list.append(DataFrame({"mi": qc_mi, "mp": qc_mp}, columns=["mi", "mp"]))
    return qc_list, data_list

def print_Qc_results(data_list):
    methods = ["Runge Kutta 4", "Runge Kutta 2", "Euler", "Euler modified"]
    print("\n\n\n***********************************\nQc tables for mi and mp\n***********************************")
    for i in range(len(methods)):
        print("\n___________________________________\n"+ methods[i] + ":")
        print(data_list[i])

def plot_results(sister_cols_list, qc_list):
    i = 0
    for sister_cols in sister_cols_list:
        for cols in sister_cols:
            plot_concentrations_continuous(cols)
            plot_concentrations_discrete(cols)
            plot_all(cols)
        qc_mi_mp = qc_list[i]
        plot_qc(qc_mi_mp[0])
        plot_qc(qc_mi_mp[1])
        i += 1
