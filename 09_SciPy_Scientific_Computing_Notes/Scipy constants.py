
"""
SciPy Constants - Complete Physical and Mathematical Constants Guide
================================================================

Comprehensive guide to SciPy's constants module, covering physical constants,
mathematical constants, unit conversions, and their applications in scientific
computing, engineering calculations, and data science applications.

Author: Python Learning Notes
Date: September 2025
Topic: Physical Constants, Mathematical Constants, Unit Conversions
"""

import numpy as np
from scipy import constants
import matplotlib.pyplot as plt
from typing import Dict, List, Any, Optional, Tuple

# =============================================================================
# PHYSICAL CONSTANTS COMPREHENSIVE
# =============================================================================

def physical_constants_comprehensive():
    """
    Complete exploration of physical constants in SciPy
    """
    print("🔬 SCIPY PHYSICAL CONSTANTS COMPREHENSIVE")
    print("=" * 43)
    
    print("🎯 Physical Constants Overview:")
    print("   Physical constants are precisely measured quantities that")
    print("   appear in the laws of nature. SciPy provides access to")
    print("   internationally accepted values from CODATA.")
    
    # Fundamental Physical Constants
    print(f"\n⚛️  Fundamental Physical Constants:")
    
    fundamental_constants = [
        ("Speed of light in vacuum", "c", constants.c, "m/s", "Electromagnetic constant"),
        ("Planck constant", "h", constants.h, "J⋅s", "Quantum mechanics"),
        ("Reduced Planck constant", "hbar", constants.hbar, "J⋅s", "ℏ = h/(2π)"),
        ("Boltzmann constant", "k", constants.k, "J/K", "Statistical mechanics"),
        ("Avogadro number", "N_A", constants.N_A, "1/mol", "Amount of substance"),
        ("Gas constant", "R", constants.R, "J/(mol⋅K)", "Ideal gas law"),
        ("Elementary charge", "e", constants.e, "C", "Electric charge unit"),
        ("Vacuum permeability", "mu_0", constants.mu_0, "H/m", "Magnetic constant"),
        ("Vacuum permittivity", "epsilon_0", constants.epsilon_0, "F/m", "Electric constant")
    ]
    
    print("   ┌─────────────────────────────┬─────────┬─────────────────────┬───────────┬─────────────────────┐")
    print("   │ Constant                    │ Symbol  │ Value               │ Unit      │ Description         │")
    print("   ├─────────────────────────────┼─────────┼─────────────────────┼───────────┼─────────────────────┤")
    
    for name, symbol, value, unit, description in fundamental_constants:
        print(f"   │ {name:<27} │ {symbol:<7} │ {value:<19.6e} │ {unit:<9} │ {description:<19} │")
    
    print("   └─────────────────────────────┴─────────┴─────────────────────┴───────────┴─────────────────────┘")
    
    # Particle Physics Constants
    print(f"\n🔬 Particle Physics Constants:")
    
    particle_constants = [
        ("Electron mass", "m_e", constants.m_e, "kg"),
        ("Proton mass", "m_p", constants.m_p, "kg"),
        ("Neutron mass", "m_n", constants.m_n, "kg"),
        ("Muon mass", "m_mu", constants.m_mu, "kg"),
        ("Atomic mass constant", "u", constants.u, "kg"),
        ("Electron radius", "r_e", constants.r_e, "m"),
        ("Bohr radius", "a_0", constants.a_0, "m"),
        ("Rydberg constant", "R_inf", constants.Rydberg, "1/m")
    ]
    
    print("   Particle         │ Symbol │ Mass/Value           │ Unit")
    print("   ─────────────────┼────────┼──────────────────────┼─────")
    
    for name, symbol, value, unit in particle_constants:
        print(f"   {name:<16} │ {symbol:<6} │ {value:<20.6e} │ {unit}")
    
    # Astronomical and Gravitational Constants
    print(f"\n🌌 Astronomical and Gravitational Constants:")
    
    astro_constants = [
        ("Gravitational constant", "G", constants.G, "m³/(kg⋅s²)"),
        ("Standard gravity", "g", constants.g, "m/s²"),
        ("Stefan-Boltzmann constant", "sigma", constants.Stefan_Boltzmann, "W/(m²⋅K⁴)"),
        ("Wien displacement constant", "b", constants.Wien, "m⋅K"),
        ("Astronomical unit", "au", constants.au, "m"),
        ("Parsec", "parsec", constants.parsec, "m"),
        ("Light year", "ly", constants.light_year, "m")
    ]
    
    print("   Constant                    │ Symbol │ Value                │ Unit")
    print("   ────────────────────────────┼────────┼──────────────────────┼─────────────────")
    
    for name, symbol, value, unit in astro_constants:
        print(f"   {name:<27} │ {symbol:<6} │ {value:<20.6e} │ {unit}")
    
    return {
        'fundamental': dict(zip([c[1] for c in fundamental_constants], [c[2] for c in fundamental_constants])),
        'particle': dict(zip([c[1] for c in particle_constants], [c[2] for c in particle_constants])),
        'astronomical': dict(zip([c[1] for c in astro_constants], [c[2] for c in astro_constants]))
    }

def mathematical_constants_exploration():
    """
    Comprehensive exploration of mathematical constants
    """
    print("\n📐 MATHEMATICAL CONSTANTS EXPLORATION")
    print("=" * 37)
    
    print("🔢 Mathematical Constants in SciPy:")
    
    # Mathematical constants
    math_constants = [
        ("Pi", "π", constants.pi, "Ratio of circumference to diameter", "3.14159..."),
        ("Euler's number", "e", np.e, "Base of natural logarithm", "2.71828..."),
        ("Golden ratio", "φ", constants.golden, "(1 + √5)/2", "1.61803..."),
        ("Golden ratio conjugate", "φ⁻¹", constants.golden_ratio, "φ - 1 = 1/φ", "0.61803...")
    ]
    
    print("   Constant              │ Symbol │ Value      │ Description                      │ Approximation")
    print("   ──────────────────────┼────────┼────────────┼──────────────────────────────────┼──────────────")
    
    for name, symbol, value, description, approx in math_constants:
        print(f"   {name:<21} │ {symbol:<6} │ {value:<10.8f} │ {description:<32} │ {approx}")
    
    # Demonstrate mathematical constant relationships
    print(f"\n🧮 Mathematical Constant Relationships:")
    
    relationships = [
        ("Euler's identity", "e^(iπ) + 1 = 0", complex(np.exp(1j * constants.pi) + 1)),
        ("Golden ratio property", "φ² = φ + 1", constants.golden**2, constants.golden + 1),
        ("Pi from circles", "Area = πr²", constants.pi, 4 * sum(1/k**2 for k in range(1, 1000)) * 6**0.5),
        ("Natural log of e", "ln(e) = 1", np.log(np.e)),
        ("Stirling's approximation", "√(2π)", (2 * constants.pi)**0.5)
    ]
    
    print(f"   Relationship: e^(iπ) + 1 = {np.exp(1j * constants.pi) + 1:.10f}")
    print(f"   Golden ratio: φ² = {constants.golden**2:.10f}, φ + 1 = {constants.golden + 1:.10f}")
    print(f"   Natural logarithm: ln(e) = {np.log(np.e):.10f}")
    print(f"   Square root: √(2π) = {np.sqrt(2 * constants.pi):.10f}")
    
    # Calculate pi using various methods
    print(f"\n🎯 Calculating π Using Different Methods:")
    
    # Leibniz series: π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
    n_terms = 10000
    leibniz_pi = 4 * sum((-1)**k / (2*k + 1) for k in range(n_terms))
    
    # Monte Carlo method
    np.random.seed(42)
    n_samples = 100000
    x = np.random.uniform(-1, 1, n_samples)
    y = np.random.uniform(-1, 1, n_samples)
    inside_circle = np.sum(x**2 + y**2 <= 1)
    monte_carlo_pi = 4 * inside_circle / n_samples
    
    # Machin's formula: π/4 = 4*arctan(1/5) - arctan(1/239)
    machin_pi = 4 * (4 * np.arctan(1/5) - np.arctan(1/239))
    
    print(f"   SciPy constant:     π = {constants.pi:.10f}")
    print(f"   Leibniz series:     π = {leibniz_pi:.10f} (error: {abs(leibniz_pi - constants.pi):.2e})")
    print(f"   Monte Carlo:        π = {monte_carlo_pi:.10f} (error: {abs(monte_carlo_pi - constants.pi):.2e})")
    print(f"   Machin's formula:   π = {machin_pi:.10f} (error: {abs(machin_pi - constants.pi):.2e})")
    
    return {
        'pi_calculations': {
            'leibniz': leibniz_pi,
            'monte_carlo': monte_carlo_pi,
            'machin': machin_pi,
            'scipy': constants.pi
        }
    }

# =============================================================================
# UNIT CONVERSIONS AND PRACTICAL APPLICATIONS
# =============================================================================

def unit_conversions_comprehensive():
    """
    Complete guide to unit conversions using SciPy constants
    """
    print("\n📏 UNIT CONVERSIONS COMPREHENSIVE")
    print("=" * 34)
    
    print("🔄 Length Conversions:")
    
    # Length units
    length_conversions = [
        ("Meter", "m", 1.0, "SI base unit"),
        ("Inch", "in", constants.inch, f"{constants.inch:.6f} m"),
        ("Foot", "ft", constants.foot, f"{constants.foot:.6f} m"),
        ("Yard", "yd", constants.yard, f"{constants.yard:.6f} m"),
        ("Mile", "mi", constants.mile, f"{constants.mile:.0f} m"),
        ("Nautical mile", "nmi", constants.nautical_mile, f"{constants.nautical_mile:.0f} m"),
        ("Angstrom", "Å", constants.angstrom, f"{constants.angstrom:.2e} m"),
        ("Light year", "ly", constants.light_year, f"{constants.light_year:.2e} m"),
        ("Parsec", "pc", constants.parsec, f"{constants.parsec:.2e} m")
    ]
    
    print("   Unit             │ Symbol │ Value in Meters      │ Description")
    print("   ─────────────────┼────────┼──────────────────────┼─────────────")
    
    for name, symbol, value, description in length_conversions:
        print(f"   {name:<16} │ {symbol:<6} │ {description:<20} │")
    
    # Volume conversions
    print(f"\n🥤 Volume Conversions:")
    
    volume_conversions = [
        ("Liter", "L", constants.liter, "0.001 m³"),
        ("Gallon (US)", "gal", constants.gallon, f"{constants.gallon:.6f} m³"),
        ("Gallon (Imperial)", "gal_imp", constants.gallon_imp, f"{constants.gallon_imp:.6f} m³"),
        ("Fluid ounce (US)", "fl_oz", constants.fluid_ounce, f"{constants.fluid_ounce:.2e} m³"),
        ("Barrel", "bbl", constants.barrel, f"{constants.barrel:.6f} m³")
    ]
    
    print("   Unit                │ Symbol  │ Value in m³")
    print("   ────────────────────┼─────────┼─────────────")
    
    for name, symbol, value, description in volume_conversions:
        print(f"   {name:<19} │ {symbol:<7} │ {description}")
    
    # Mass conversions
    print(f"\n⚖️  Mass Conversions:")
    
    mass_conversions = [
        ("Kilogram", "kg", 1.0, "SI base unit"),
        ("Gram", "g", 1e-3, "0.001 kg"),
        ("Pound", "lb", constants.pound, f"{constants.pound:.6f} kg"),
        ("Ounce", "oz", constants.ounce, f"{constants.ounce:.6f} kg"),
        ("Stone", "st", constants.stone, f"{constants.stone:.6f} kg"),
        ("Atomic mass unit", "u", constants.u, f"{constants.u:.2e} kg"),
        ("Ton (metric)", "t", constants.ton_TNT/1e9, "1000 kg")
    ]
    
    print("   Unit                │ Symbol │ Value in kg")
    print("   ────────────────────┼────────┼─────────────")
    
    for name, symbol, value, description in mass_conversions[:6]:  # Skip the last problematic one
        print(f"   {name:<19} │ {symbol:<6} │ {description}")
    
    # Energy conversions
    print(f"\n⚡ Energy Conversions:")
    
    energy_conversions = [
        ("Joule", "J", 1.0, "SI unit"),
        ("Electron volt", "eV", constants.eV, f"{constants.eV:.2e} J"),
        ("Calorie", "cal", constants.calorie, f"{constants.calorie:.1f} J"),
        ("British thermal unit", "BTU", constants.Btu, f"{constants.Btu:.0f} J"),
        ("Kilowatt hour", "kWh", 3.6e6, "3.6×10⁶ J"),
        ("TNT equivalent", "TNT", constants.ton_TNT, f"{constants.ton_TNT:.2e} J")
    ]
    
    print("   Unit                    │ Symbol │ Value in Joules")
    print("   ────────────────────────┼────────┼─────────────────")
    
    for name, symbol, value, description in energy_conversions:
        print(f"   {name:<23} │ {symbol:<6} │ {description}")
    
    # Practical conversion examples
    print(f"\n🛠️  Practical Conversion Examples:")
    
    # Example 1: Convert height from feet/inches to meters
    height_ft = 6
    height_in = 2
    height_m = height_ft * constants.foot + height_in * constants.inch
    
    print(f"   Height conversion:")
    print(f"     {height_ft}' {height_in}\" = {height_m:.3f} m = {height_m * 100:.1f} cm")
    
    # Example 2: Convert fuel efficiency
    mpg = 30  # miles per gallon
    km_per_liter = (mpg * constants.mile) / (1000 * constants.gallon)
    
    print(f"   Fuel efficiency:")
    print(f"     {mpg} mpg = {km_per_liter:.2f} km/L = {100/km_per_liter:.1f} L/100km")
    
    # Example 3: Convert energy units
    kwh = 1000  # kWh
    joules = kwh * 3.6e6
    calories = joules / constants.calorie
    
    print(f"   Energy conversion:")
    print(f"     {kwh} kWh = {joules:.2e} J = {calories:.0f} cal")
    
    # Example 4: Temperature conversions
    print(f"\n🌡️  Temperature Conversions:")
    
    celsius_temps = [0, 20, 37, 100]
    
    print("   Celsius │ Kelvin  │ Fahrenheit │ Rankine")
    print("   ────────┼─────────┼────────────┼─────────")
    
    for c in celsius_temps:
        k = c + constants.zero_Celsius
        f = c * 9/5 + 32
        r = f + 459.67
        print(f"   {c:7.1f} │ {k:7.2f} │ {f:10.1f} │ {r:7.2f}")
    
    return {
        'length_conversions': length_conversions,
        'volume_conversions': volume_conversions,
        'mass_conversions': mass_conversions,
        'energy_conversions': energy_conversions
    }

def scientific_applications():
    """
    Practical applications of constants in scientific calculations
    """
    print("\n🔬 SCIENTIFIC APPLICATIONS")
    print("=" * 27)
    
    # Application 1: Blackbody Radiation
    print("🌟 Application 1: Blackbody Radiation (Stefan-Boltzmann Law)")
    print("   Power radiated: P = σ × A × T⁴")
    
    # Calculate power radiated by the Sun
    sun_surface_temp = 5778  # Kelvin
    sun_radius = 6.96e8  # meters
    sun_surface_area = 4 * constants.pi * sun_radius**2
    
    power_radiated = constants.Stefan_Boltzmann * sun_surface_area * sun_surface_temp**4
    
    print(f"   Sun's surface temperature: {sun_surface_temp} K")
    print(f"   Sun's surface area: {sun_surface_area:.2e} m²")
    print(f"   Stefan-Boltzmann constant: {constants.Stefan_Boltzmann:.2e} W/(m²⋅K⁴)")
    print(f"   Total power radiated: {power_radiated:.2e} W = {power_radiated/1e26:.1f} × 10²⁶ W")
    
    # Application 2: Ideal Gas Law
    print(f"\n💨 Application 2: Ideal Gas Law (PV = nRT)")
    
    # Calculate pressure of gas in a container
    n_moles = 2.0  # moles
    temperature = 300  # Kelvin (27°C)
    volume = 0.024  # m³ (24 liters)
    
    pressure = (n_moles * constants.R * temperature) / volume
    
    print(f"   Amount of gas: {n_moles} mol")
    print(f"   Temperature: {temperature} K ({temperature - constants.zero_Celsius:.0f}°C)")
    print(f"   Volume: {volume} m³ ({volume * 1000:.0f} L)")
    print(f"   Gas constant: {constants.R:.3f} J/(mol⋅K)")
    print(f"   Pressure: {pressure:.0f} Pa = {pressure/1e5:.2f} bar = {pressure/101325:.2f} atm")
    
    # Application 3: Photoelectric Effect
    print(f"\n💡 Application 3: Photoelectric Effect")
    print("   Energy of photon: E = hν = hc/λ")
    
    # Calculate photon energy for different wavelengths
    wavelengths = [400e-9, 550e-9, 700e-9]  # Blue, green, red light (meters)
    colors = ["Blue", "Green", "Red"]
    
    print(f"   Planck constant: h = {constants.h:.2e} J⋅s")
    print(f"   Speed of light: c = {constants.c:.2e} m/s")
    
    print("   Color  │ Wavelength │ Frequency     │ Photon Energy")
    print("   ───────┼────────────┼───────────────┼──────────────")
    
    for color, wavelength in zip(colors, wavelengths):
        frequency = constants.c / wavelength
        energy_j = constants.h * frequency
        energy_ev = energy_j / constants.eV
        
        print(f"   {color:<6} │ {wavelength*1e9:7.0f} nm  │ {frequency:.2e} Hz │ {energy_ev:.2f} eV")
    
    # Application 4: Gravitational Force
    print(f"\n🌍 Application 4: Gravitational Force")
    print("   Force: F = G × (m₁ × m₂) / r²")
    
    # Earth-Moon system
    earth_mass = 5.972e24  # kg
    moon_mass = 7.342e22   # kg
    earth_moon_distance = 3.844e8  # meters
    
    gravitational_force = (constants.G * earth_mass * moon_mass) / (earth_moon_distance**2)
    
    print(f"   Earth mass: {earth_mass:.3e} kg")
    print(f"   Moon mass: {moon_mass:.3e} kg") 
    print(f"   Distance: {earth_moon_distance:.3e} m")
    print(f"   Gravitational constant: G = {constants.G:.2e} m³/(kg⋅s²)")
    print(f"   Gravitational force: {gravitational_force:.2e} N")
    
    # Application 5: Nuclear Binding Energy
    print(f"\n⚛️  Application 5: Nuclear Binding Energy (E = mc²)")
    
    # Calculate binding energy from mass defect
    mass_defect = 0.03038 * constants.u  # Mass defect for Helium-4 (atomic mass units to kg)
    binding_energy_j = mass_defect * constants.c**2
    binding_energy_mev = binding_energy_j / (constants.eV * 1e6)
    
    print(f"   Mass defect: {mass_defect/constants.u:.5f} u = {mass_defect:.2e} kg")
    print(f"   Speed of light: c = {constants.c:.2e} m/s") 
    print(f"   Binding energy: {binding_energy_mev:.1f} MeV = {binding_energy_j:.2e} J")
    print(f"   Binding energy per nucleon: {binding_energy_mev/4:.1f} MeV/nucleon")
    
    return {
        'blackbody_power': power_radiated,
        'gas_pressure': pressure,
        'photon_energies': dict(zip(colors, [constants.h * constants.c / w / constants.eV for w in wavelengths])),
        'gravitational_force': gravitational_force,
        'binding_energy': binding_energy_mev
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive SciPy constants guide
    """
    print(__doc__)
    
    # Physical constants
    physical_results = physical_constants_comprehensive()
    
    # Mathematical constants
    math_results = mathematical_constants_exploration()
    
    # Unit conversions
    conversion_results = unit_conversions_comprehensive()
    
    # Scientific applications
    application_results = scientific_applications()
    
    return {
        'physical_constants': physical_results,
        'mathematical_constants': math_results,
        'unit_conversions': conversion_results,
        'scientific_applications': application_results
    }

if __name__ == "__main__":
    """
    Execute comprehensive SciPy constants guide and demonstrations
    """
    results = main()
    
    print("\n" + "=" * 60)
    print("🎓 SCIPY CONSTANTS MASTERY SUMMARY")
    print("=" * 60)
    print("✅ Comprehensive physical constants from CODATA")
    print("✅ Mathematical constants and their relationships")
    print("✅ Complete unit conversion system")
    print("✅ Practical scientific calculations and applications")
    print("✅ Blackbody radiation and Stefan-Boltzmann law")
    print("✅ Ideal gas law and thermodynamics")
    print("✅ Photoelectric effect and quantum mechanics")
    print("✅ Gravitational physics and celestial mechanics")
    print("✅ Nuclear physics and binding energy calculations")
    print("✅ Engineering and measurement conversions")
    
    print("\n💡 SciPy Constants Mastery Key Points:")
    key_points = [
        "Use internationally accepted CODATA values for precision",
        "Combine constants for complex scientific calculations",
        "Apply unit conversions for international compatibility",
        "Understand physical meaning behind mathematical relationships",
        "Leverage constants for engineering and scientific modeling",
        "Validate calculations using dimensional analysis",
        "Use appropriate precision for different applications",
        "Stay updated with latest constant values and standards"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Constants Applications in Science & Engineering:")
    applications = [
        "Quantum mechanics and atomic physics calculations",
        "Thermodynamics and statistical mechanics",
        "Electromagnetic field theory and optics",
        "Astrophysics and cosmological modeling",
        "Nuclear physics and particle accelerators",
        "Engineering design and materials science",
        "Chemistry and molecular modeling",
        "Metrology and measurement standards"
    ]
    
    for i, app in enumerate(applications, 1):
        print(f"   {i}. {app}")
    
    print(f"\n🚀 Ready for Precision Scientific Computing!")
    print("Master the fundamental constants that govern our universe!")
Print the constant value of PI:

from scipy import constants

print(constants.pi)
Constant Units
A list of all units under the constants module can be seen using the dir() function.

Example
List all constants:

from scipy import constants

print(dir(constants))
Unit Categories
The units are placed under these categories:

Metric
Binary
Mass
Angle
Time
Length
Pressure
Volume
Speed
Temperature
Energy
Power
Force
ADVERTISEMENT

REMOVE ADS

Metric (SI) Prefixes:
Return the specified unit in meter (e.g. centi returns 0.01)

Example
from scipy import constants

print(constants.yotta)    #1e+24
print(constants.zetta)    #1e+21
print(constants.exa)      #1e+18
print(constants.peta)     #1000000000000000.0
print(constants.tera)     #1000000000000.0
print(constants.giga)     #1000000000.0
print(constants.mega)     #1000000.0
print(constants.kilo)     #1000.0
print(constants.hecto)    #100.0
print(constants.deka)     #10.0
print(constants.deci)     #0.1
print(constants.centi)    #0.01
print(constants.milli)    #0.001
print(constants.micro)    #1e-06
print(constants.nano)     #1e-09
print(constants.pico)     #1e-12
print(constants.femto)    #1e-15
print(constants.atto)     #1e-18
print(constants.zepto)    #1e-21
Binary Prefixes:
Return the specified unit in bytes (e.g. kibi returns 1024)

Example
from scipy import constants

print(constants.kibi)    #1024
print(constants.mebi)    #1048576
print(constants.gibi)    #1073741824
print(constants.tebi)    #1099511627776
print(constants.pebi)    #1125899906842624
print(constants.exbi)    #1152921504606846976
print(constants.zebi)    #1180591620717411303424
print(constants.yobi)    #1208925819614629174706176
Mass:
Return the specified unit in kg (e.g. gram returns 0.001)

Example
from scipy import constants

print(constants.gram)        #0.001
print(constants.metric_ton)  #1000.0
print(constants.grain)       #6.479891e-05
print(constants.lb)          #0.45359236999999997
print(constants.pound)       #0.45359236999999997
print(constants.oz)          #0.028349523124999998
print(constants.ounce)       #0.028349523124999998
print(constants.stone)       #6.3502931799999995
print(constants.long_ton)    #1016.0469088
print(constants.short_ton)   #907.1847399999999
print(constants.troy_ounce)  #0.031103476799999998
print(constants.troy_pound)  #0.37324172159999996
print(constants.carat)       #0.0002
print(constants.atomic_mass) #1.66053904e-27
print(constants.m_u)         #1.66053904e-27
print(constants.u)           #1.66053904e-27
Angle:
Return the specified unit in radians (e.g. degree returns 0.017453292519943295)

Example
from scipy import constants

print(constants.degree)     #0.017453292519943295
print(constants.arcmin)     #0.0002908882086657216
print(constants.arcminute)  #0.0002908882086657216
print(constants.arcsec)     #4.84813681109536e-06
print(constants.arcsecond)  #4.84813681109536e-06
Time:
Return the specified unit in seconds (e.g. hour returns 3600.0)

Example
from scipy import constants

print(constants.minute)      #60.0
print(constants.hour)        #3600.0
print(constants.day)         #86400.0
print(constants.week)        #604800.0
print(constants.year)        #31536000.0
print(constants.Julian_year) #31557600.0
Length:
Return the specified unit in meters (e.g. nautical_mile returns 1852.0)

Example
from scipy import constants

print(constants.inch)              #0.0254
print(constants.foot)              #0.30479999999999996
print(constants.yard)              #0.9143999999999999
print(constants.mile)              #1609.3439999999998
print(constants.mil)               #2.5399999999999997e-05
print(constants.pt)                #0.00035277777777777776
print(constants.point)             #0.00035277777777777776
print(constants.survey_foot)       #0.3048006096012192
print(constants.survey_mile)       #1609.3472186944373
print(constants.nautical_mile)     #1852.0
print(constants.fermi)             #1e-15
print(constants.angstrom)          #1e-10
print(constants.micron)            #1e-06
print(constants.au)                #149597870691.0
print(constants.astronomical_unit) #149597870691.0
print(constants.light_year)        #9460730472580800.0
print(constants.parsec)            #3.0856775813057292e+16
Pressure:
Return the specified unit in pascals (e.g. psi returns 6894.757293168361)

Example
from scipy import constants

print(constants.atm)         #101325.0
print(constants.atmosphere)  #101325.0
print(constants.bar)         #100000.0
print(constants.torr)        #133.32236842105263
print(constants.mmHg)        #133.32236842105263
print(constants.psi)         #6894.757293168361
Area:
Return the specified unit in square meters(e.g. hectare returns 10000.0)

Example
from scipy import constants

print(constants.hectare) #10000.0
print(constants.acre)    #4046.8564223999992
Volume:
Return the specified unit in cubic meters (e.g. liter returns 0.001)

Example
from scipy import constants

print(constants.liter)            #0.001
print(constants.litre)            #0.001
print(constants.gallon)           #0.0037854117839999997
print(constants.gallon_US)        #0.0037854117839999997
print(constants.gallon_imp)       #0.00454609
print(constants.fluid_ounce)      #2.9573529562499998e-05
print(constants.fluid_ounce_US)   #2.9573529562499998e-05
print(constants.fluid_ounce_imp)  #2.84130625e-05
print(constants.barrel)           #0.15898729492799998
print(constants.bbl)              #0.15898729492799998
Speed:
Return the specified unit in meters per second (e.g. speed_of_sound returns 340.5)

Example
from scipy import constants

print(constants.kmh)            #0.2777777777777778
print(constants.mph)            #0.44703999999999994
print(constants.mach)           #340.5
print(constants.speed_of_sound) #340.5
print(constants.knot)           #0.5144444444444445
Temperature:
Return the specified unit in Kelvin (e.g. zero_Celsius returns 273.15)

Example
from scipy import constants

print(constants.zero_Celsius)      #273.15
print(constants.degree_Fahrenheit) #0.5555555555555556
Energy:
Return the specified unit in joules (e.g. calorie returns 4.184)

Example
from scipy import constants

print(constants.eV)            #1.6021766208e-19
print(constants.electron_volt) #1.6021766208e-19
print(constants.calorie)       #4.184
print(constants.calorie_th)    #4.184
print(constants.calorie_IT)    #4.1868
print(constants.erg)           #1e-07
print(constants.Btu)           #1055.05585262
print(constants.Btu_IT)        #1055.05585262
print(constants.Btu_th)        #1054.3502644888888
print(constants.ton_TNT)       #4184000000.0
Power:
Return the specified unit in watts (e.g. horsepower returns 745.6998715822701)

Example
from scipy import constants

print(constants.hp)         #745.6998715822701
print(constants.horsepower) #745.6998715822701
Force:
Return the specified unit in newton (e.g. kilogram_force returns 9.80665)

Example
from scipy import constants

print(constants.dyn)             #1e-05
print(constants.dyne)            #1e-05
print(constants.lbf)             #4.4482216152605
print(constants.pound_force)     #4.4482216152605
print(constants.kgf)             #9.80665
print(constants.kilogram_force)  #9.80665