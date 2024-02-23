from pythlete import safetycar
from pythlete import telemetry
from pythlete import general
from pythlete import pitstop
from pythlete import strategy

# run the simulation with and without safety car
safetycar.simulation_results(1, 'NED', 'HAM', safety_car = 0)
safetycar.simulation_results(1, 'NED', 'HAM', safety_car = 1)


#first step is to load the session
session = general.load_session(2021, 'Spanish Grand Prix', 'Q')
# get circuit information
circuit_info = telemetry.circuit_info(session)
# get fastest laps for the two drivers
ham_lap = telemetry.pick_fastest_laps('HAM', session)
lec_lap = telemetry.pick_fastest_laps('LEC', session)
# add distance to the fastest laps
ham_lap = telemetry.add_distance_to_lap(ham_lap)
lec_lap = telemetry.add_distance_to_lap(lec_lap)
# prepare the dataframe for plotting and comparison
tel = telemetry.prepare_dataframe(ham_lap, lec_lap, session)
# find the loss and gain for the the driver of interest
telemetry.find_loss(tel, 'HAM')
telemetry.find_gain(tel, 'HAM')
# plot the laps
telemetry.plot_laps(ham_lap, lec_lap, 'MER', 'FER', session)



# load the session first
session = general.load_session(2023, 'Spanish Grand Prix', 'R')
ham_laps = pitstop.get_laps('HAM', session)
lec_laps = pitstop.get_laps('LEC', session)
# preprocess the dataframe
ham_laps = general.data_pre_processing(ham_laps)
lec_laps = general.data_pre_processing(lec_laps)
# plot the lap time for each driver
pitstop.plot_lap_times(ham_laps, session)
pitstop.plot_lap_times(lec_laps, session)
# prepare the dataframe for comparison
combined_dataframe = pitstop.prepare_dataframe(ham_laps, lec_laps)
# plot the lap time difference
pitstop.plot_lap_time_difference(combined_dataframe, ham_laps, lec_laps, session)
# print the pit stop recommendation
pit_laps = pitstop.when_to_pit(combined_dataframe, ham_laps, lec_laps)
# plot the race progress
pitstop.plot_both_drivers(ham_laps, lec_laps, session, 'MER', 'FER', pit_laps)


# load the session first
race = 'Monaco Grand Prix'
year = 2021
sessions = strategy.load_practices(year, race)
# pick the driver's data
practices = strategy.process_practice_data('HAM', sessions)
# define the distributions for the practice data
distributions = strategy.practice_data_distributions(practices)
# plot the practice data distributions
strategy.plot_practice_distributions(practices, distributions)
# define the object for the race simulation
Monaco = strategy.Race(['MEDIUM', 'SOFT', 'HARD'], 22, 78, distributions, race, threshold_value = 0.7)
# run the simulation
Monaco.run()
# print the stints
print(Monaco.stints)
# get the lap times
lap_times_df = strategy.get_race_stats(Monaco)
# plot the tire performance
strategy.plot_simulated_tire_performance(lap_times_df)
# plot the lap times
strategy.plot_simulated_lap_times(lap_times_df)
# load the actual race
actual_race = general.load_session(year, race, 'R')
# call the comparison function
strategy.compare_results(actual_race, Monaco)