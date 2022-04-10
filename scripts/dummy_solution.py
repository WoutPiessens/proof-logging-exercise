"""
Complete solution
"""


def query_01(connection, column_names, X=350):
    # Bouw je query
    query = """
    SELECT m.nameFirst, m.nameLast, h.yearid, h.votes
FROM HallOfFame h, Master m 
WHERE h.playerID=m.playerID AND h.votes> {X}
ORDER BY m.nameFirst, m.nameLast, h.yearid, h.votes DESC;
    """.format(
        X=X
    )

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_02(connection, column_names, X="AL"):
    # Bouw je query
    query = "Maak je query hier"

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


def query_03(connection, column_names, X="AL", Y="W", N=1975, M=1985):
    # Bouw je query
    query = "Maak je query hier"

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 04
def query_04(connection, column_names, X=50, Y=1900):
    # Bouw je query
    query = "Maak je query hier"
    

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


#
# def query_04_v_02(connection, column_names, X=3):
#     # Bouw je query
#     query = """
#     SELECT
#         P.nameLast,
#         P.nameFirst,
#         M.teamID,
#         COUNT(DISTINCT M.yearID) as NumYears,
#         AVG(W) as AvgW,
#         AVG(rank) as AvgR
#     FROM
#         Managers as M,
#         Master as P
#     WHERE
#         M.playerID=P.playerID
#     GROUP BY
#         M.playerID,
#         M.teamID
#     HAVING
#         COUNT(DISTINCT M.yearID) >= {X}
#     ORDER BY
#         AvgR,
#         NumYears DESC,
#         AvgW DESC,
#         M.teamID,
#         P.nameLast,
#         P.nameFirst;
#     """.format(
#         X=X
#     )
#
#     # Stap 2 & 3
#     res = run_query(connection, query)  # Query uitvoeren
#     df = res_to_df(res, column_names)  # Query in DataFrame brengen
#
#     return df


# Query 05
def query_05(connection, column_names, X=3, Y=50):
    # Bouw je query
    query = "Maak je query hier"

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 06
def query_06(connection, column_names, X=500, Y=500, Z=5):
    # Bouw je query
    query = "Maak je query hier"

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 07
def query_07(connection, column_names, X=3):
    # Bouw je query
    query = "Maak je query hier"

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df


# Query 08
def query_08(connection, column_names, N=8):
    # Bouw je query
    query = "Maak je query hier"

    # Stap 2 & 3
    res = run_query(connection, query)  # Query uitvoeren
    df = res_to_df(res, column_names)  # Query in DataFrame brengen

    return df
