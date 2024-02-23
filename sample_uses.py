from pythlete import safetycar
from pythlete import telemetry
from pythlete import general
from pythlete import pitstop

# # run the simulation with and without safety car
# safetycar.simulation_results(1, 'NED', 'HAM', safety_car = 0)
# safetycar.simulation_results(1, 'NED', 'HAM', safety_car = 1)


# #first step is to load the session
# session = general.load_session(2021, 'Spanish Grand Prix', 'Q')
# # get circuit information
# circuit_info = telemetry.circuit_info(session)
# # get fastest laps for the two drivers
# ham_lap = telemetry.pick_fastest_laps('HAM', session)
# lec_lap = telemetry.pick_fastest_laps('LEC', session)
# # add distance to the fastest laps
# ham_lap = telemetry.add_distance_to_lap(ham_lap)
# lec_lap = telemetry.add_distance_to_lap(lec_lap)
# # prepare the dataframe for plotting and comparison
# tel = telemetry.prepare_dataframe(ham_lap, lec_lap, session)
# # find the loss and gain for the the driver of interest
# telemetry.find_loss(tel, 'HAM')
# telemetry.find_gain(tel, 'HAM')
# # plot the laps
# telemetry.plot_laps(ham_lap, lec_lap, 'MER', 'FER', session)



# # load the session first
# session = general.load_session(2023, 'Spanish Grand Prix', 'R')
# ham_laps = pitstop.get_laps('HAM', session)
# lec_laps = pitstop.get_laps('LEC', session)
# # preprocess the dataframe
# ham_laps = general.data_pre_processing(ham_laps)
# lec_laps = general.data_pre_processing(lec_laps)
# # plot the lap time for each driver
# pitstop.plot_lap_times(ham_laps, session)
# pitstop.plot_lap_times(lec_laps, session)
# # prepare the dataframe for comparison
# combined_dataframe = pitstop.prepare_dataframe(ham_laps, lec_laps)
# # plot the lap time difference
# pitstop.plot_lap_time_difference(combined_dataframe, ham_laps, lec_laps, session)
# # print the pit stop recommendation
# pit_laps = pitstop.when_to_pit(combined_dataframe, ham_laps, lec_laps)
# # plot the race progress
# pitstop.plot_both_drivers(ham_laps, lec_laps, session, 'MER', 'FER', pit_laps)

