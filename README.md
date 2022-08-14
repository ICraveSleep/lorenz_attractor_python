# Lorenz Attractor
Lorenz Equations

$$
    \dot x = \sigma (y-x)
$$
$$
    \dot y = x(\rho - z) -y
$$
$$
    \dot z = xy - \beta z
$$
For the Lorenz attractor with the butterfly wing shape:
$$
    \sigma = 10, ~~ \beta = \frac{8}{3}, ~~ \rho = 28
$$


<p align="center">
    <img src="misc/figures/lorenz_attractor_image.PNG"/>
</p>

Runge-Kutta 4 weighing used.

$$
     y_{k+1} = y_k + \frac{\Delta t}{6} \left(f_1 + 2f_2 + 2f_3 + f_4\right)+\mathcal{O}(\Delta t^5)
$$

$$
    f_1 = \dot y(t) = f(t_k, y_k)
$$

$$
    f_2 = f\left(t_k + \frac{\Delta t}{2}, y_k + \frac{\Delta t}{2} f_1\right)
$$

$$
    f_3 = f\left((t_k + \frac{\Delta t}{2}, y_k + \frac{\Delta t}{2} f_2\right)
$$

$$
    f_2 = f(t_k + \Delta t, y_k + \Delta t f_3)
$$