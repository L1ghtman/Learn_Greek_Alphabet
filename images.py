import pygame as pg
from settings import *

# import game images here
bicep_left = pg.image.load('sprites/bicep_left.png')
bicep_right = pg.image.load('sprites/bicep_right.png')
heart = pg.image.load('sprites/heart.png')
heart_dead = pg.image.load('sprites/heart_dead.png')

scaled_bicep_left = pg.transform.scale(bicep_left, (360, 360))
scaled_bicep_right = pg.transform.scale(bicep_right, (360, 360))
heart = pg.transform.scale(heart, (50, 50))
heart_dead = pg.transform.scale(heart_dead, (50, 50))

scaled_bicep_left_rect = scaled_bicep_left.get_rect()
scaled_bicep_right_rect = scaled_bicep_right.get_rect()

scaled_bicep_left_rect.center = (RES[0]//2 - 300, RES[1]//2 - 100)
scaled_bicep_right_rect.center = (RES[0]//2 + 300, RES[1]//2 - 100)

# import images of greek alphabet here
alpha_l = pg.image.load('sprites/Alpha_lower.png')
alpha_u = pg.image.load('sprites/Alpha_upper.png')
beta_l = pg.image.load('sprites/Beta_lower.png')
beta_u = pg.image.load('sprites/Beta_upper.png')
gamma_l = pg.image.load('sprites/Gamma_lower.png')
gamma_u = pg.image.load('sprites/Gamma_upper.png')
delta_l = pg.image.load('sprites/Delta_lower.png')
delta_u = pg.image.load('sprites/Delta_upper.png')
epsilon_l = pg.image.load('sprites/Epsilon_lower.png')
epsilon_u = pg.image.load('sprites/Epsilon_upper.png')
zeta_l = pg.image.load('sprites/Zeta_lower.png')
zeta_u = pg.image.load('sprites/Zeta_upper.png')
eta_l = pg.image.load('sprites/Eta_lower.png')
eta_u = pg.image.load('sprites/Eta_upper.png')
theta_l = pg.image.load('sprites/Theta_lower.png')
theta_u = pg.image.load('sprites/Theta_upper.png')
iota_l = pg.image.load('sprites/Iota_lower.png')
iota_u = pg.image.load('sprites/Iota_upper.png')
kappa_l = pg.image.load('sprites/Kappa_lower.png')
kappa_u = pg.image.load('sprites/Kappa_upper.png')
lambda_l = pg.image.load('sprites/Lambda_lower.png')
lambda_u = pg.image.load('sprites/Lambda_upper.png')
mu_l = pg.image.load('sprites/Mu_lower.png')
mu_u = pg.image.load('sprites/Mu_upper.png')
nu_l = pg.image.load('sprites/Nu_lower.png')
nu_u = pg.image.load('sprites/Nu_upper.png')
xi_l = pg.image.load('sprites/Xi_lower.png')
xi_u = pg.image.load('sprites/Xi_upper.png')
omicron_l = pg.image.load('sprites/Omicron_lower.png')
omicron_u = pg.image.load('sprites/Omicron_upper.png')
pi_l = pg.image.load('sprites/Pi_lower.png')
pi_u = pg.image.load('sprites/Pi_upper.png')
rho_l = pg.image.load('sprites/Rho_lower.png')
rho_u = pg.image.load('sprites/Rho_upper.png')
sigma_l = pg.image.load('sprites/Sigma_lower.png')
sigma_u = pg.image.load('sprites/Sigma_upper.png')
tau_l = pg.image.load('sprites/Tau_lower.png')
tau_u = pg.image.load('sprites/Tau_upper.png')
upsilon_l = pg.image.load('sprites/Upsilon_lower.png')
upsilon_u = pg.image.load('sprites/Upsilon_upper.png')
phi_l = pg.image.load('sprites/Phi_lower.png')
phi_u = pg.image.load('sprites/Phi_upper.png')
chi_l = pg.image.load('sprites/Chi_lower.png')
chi_u = pg.image.load('sprites/Chi_upper.png')
psi_l = pg.image.load('sprites/Psi_lower.png')
psi_u = pg.image.load('sprites/Psi_upper.png')
omega_l = pg.image.load('sprites/Omega_lower.png')
omega_u = pg.image.load('sprites/Omega_upper.png')

alphabet = [[alpha_u, alpha_l, 'alpha'],
            [beta_u, beta_l, 'beta'],
            [gamma_u, gamma_l, 'gamma'],
            [delta_u, delta_l, 'delta'],
            [epsilon_u, epsilon_l, 'epsilon'],
            [zeta_u, zeta_l, 'zeta'],
            [eta_u, eta_l, 'eta'],
            [theta_u, theta_l, 'theta'],
            [iota_u, iota_l, 'iota'],
            [kappa_u, kappa_l, 'kappa'],
            [lambda_u, lambda_l, 'lambda'],
            [mu_u, mu_l, 'mu'],
            [nu_u, nu_l, 'nu'],
            [xi_u, xi_l, 'xi'],
            [omicron_u, omicron_l, 'omicron'],
            [pi_u, pi_l, 'pi'],
            [rho_u, rho_l, 'rho'],
            [sigma_u, sigma_l, 'sigma'],
            [tau_u, tau_l, 'tau'],
            [upsilon_u, upsilon_l, 'upsilon'],
            [phi_u, phi_l, 'phi'],
            [chi_u, chi_l, 'chi'],
            [psi_u, psi_l, 'psi'],
            [omega_u, omega_l, 'omega']]

alpha_l_rect = alpha_l.get_rect()
alpha_u_rect = alpha_u.get_rect()
beta_l_rect = beta_l.get_rect()
beta_u_rect = beta_u.get_rect()
gamma_l_rect = gamma_l.get_rect()
gamma_u_rect = gamma_u.get_rect()
delta_l_rect = delta_l.get_rect()
delta_u_rect = delta_u.get_rect()
epsilon_l_rect = epsilon_l.get_rect()
epsilon_u_rect = epsilon_u.get_rect()
zeta_l_rect = zeta_l.get_rect()
zeta_u_rect = zeta_u.get_rect()
eta_l_rect = eta_l.get_rect()
eta_u_rect = eta_u.get_rect()
theta_l_rect = theta_l.get_rect()
theta_u_rect = theta_u.get_rect()
iota_l_rect = iota_l.get_rect()
iota_u_rect = iota_u.get_rect()
kappa_l_rect = kappa_l.get_rect()
kappa_u_rect = kappa_u.get_rect()
lambda_l_rect = lambda_l.get_rect()
lambda_u_rect = lambda_u.get_rect()
mu_l_rect = mu_l.get_rect()
mu_u_rect = mu_u.get_rect()
nu_l_rect = nu_l.get_rect()
nu_u_rect = nu_u.get_rect()
xi_l_rect = xi_l.get_rect()
xi_u_rect = xi_u.get_rect()
omicron_l_rect = omicron_l.get_rect()
omicron_u_rect = omicron_u.get_rect()
pi_l_rect = pi_l.get_rect()
pi_u_rect = pi_u.get_rect()
rho_l_rect = rho_l.get_rect()
rho_u_rect = rho_u.get_rect()
sigma_l_rect = sigma_l.get_rect()
sigma_u_rect = sigma_u.get_rect()
tau_l_rect = tau_l.get_rect()
tau_u_rect = tau_u.get_rect()
upsilon_l_rect = upsilon_l.get_rect()
upsilon_u_rect = upsilon_u.get_rect()
phi_l_rect = phi_l.get_rect()
phi_u_rect = phi_u.get_rect()
chi_l_rect = chi_l.get_rect()
chi_u_rect = chi_u.get_rect()
psi_l_rect = psi_l.get_rect()
psi_u_rect = psi_u.get_rect()
omega_l_rect = omega_l.get_rect()
omega_u_rect = omega_u.get_rect()

