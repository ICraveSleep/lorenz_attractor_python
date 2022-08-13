from matplotlib import pyplot as plt


def create_time_span(t_start, t_end, step_size):
    time_span = []
    time = t_start
    while time <= t_end:
        time_span.append(time)
        time += step_size
    time_span.append(time)
    return time_span


def sum_list(list_in):
    summed_list = len(list_in[0]) * [0]
    for a in list_in:
        for i in range(len(a)):
            summed_list[i] += a[i]
    return summed_list


def lorenz(t, y: [], sigma, beta, rho):
    # x = y[0], y = y[1], z = y[2]
    dx = sigma * (y[1] - y[0])
    dy = y[0] * (rho - y[2]) - y[1]
    dz = y[0] * y[1] - beta * y[2]
    return [dx, dy, dz]


def euler_step(dt, tk, yk: []):
    sigma = 10
    beta = 8 / 3
    rho = 28
    dyk = lorenz(tk, yk, sigma, beta, rho)
    dyk = [dt * a for a in dyk]
    return sum_list([yk, dyk])


def RK4_step(dt, tk, yk: []):
    sigma = 10
    beta = 8 / 3
    rho = 28
    f1 = lorenz(tk, yk, sigma, beta, rho)
    prem = sum_list([yk, [(dt / 2) * a for a in f1]])
    f2 = lorenz(tk + dt / 2, prem, sigma, beta, rho)
    prem = sum_list([yk, [(dt / 2) * a for a in f2]])
    f3 = lorenz(tk + dt / 2, prem, sigma, beta, rho)
    prem = sum_list([yk, [dt * a for a in f3]])
    f4 = lorenz(tk + dt, prem, sigma, beta, rho)

    f1 = [a * dt / 6 for a in f1]
    f2 = [a * dt / 3 for a in f2]
    f3 = [a * dt / 3 for a in f3]
    f4 = [a * dt / 6 for a in f4]
    prem = sum_list([yk, f1, f2, f3, f4])
    return prem


if __name__ == '__main__':
    state = [-8, 8, 27]  # x, y, z
    dt_euler = 0.00001
    dt_rk4 = 0.02
    t = 4
    rk4_timer = create_time_span(0, t, dt_rk4)
    euler_timer = create_time_span(0, t, dt_euler)

    rk4_state = state
    euler_state = state
    rk4_simulation = []
    euler_simulation = []

    tk = 0
    for i in range(len(rk4_timer)):
        tk = i * dt_rk4
        rk4_state = RK4_step(dt_rk4, tk, rk4_state)
        rk4_simulation.append(rk4_state)

    tk = 0
    for i in range(len(euler_timer)):
        tk = i * dt_euler
        euler_state = euler_step(dt_euler, tk, euler_state)
        euler_simulation.append(euler_state)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    xline = []
    yline = []
    zline = []
    xlinee = []
    ylinee = []
    zlinee = []

    for measurement in rk4_simulation:
        xline.append(measurement[0])
        yline.append(measurement[1])
        zline.append(measurement[2])
    for measurement in euler_simulation:
        xlinee.append(measurement[0])
        ylinee.append(measurement[1])
        zlinee.append(measurement[2])

    ax.plot3D(xline, yline, zline, 'gray')
    ax.plot3D(xlinee, ylinee, zlinee, 'red')
    plt.show()
