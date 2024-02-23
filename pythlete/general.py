import fastf1

def load_session(year, race, session):
    '''
    Loads the session data for a given race.

    Parameters:
    year: int
        the year of the race
    race: string
        the exact race that we are retrieving data for
    session: string
        the session that we are retrieving data for such as FP1, FP2, FP3, Q, R

    Returns:
    session_data: pandas dataframe
        the session data
    '''
    # load the session
    session = fastf1.get_session(year, race, session)
    session.load()
    
    # return session
    return session