def calculate_elo(p1_score, p2_score, p1_rating, p2_rating, K = 32.0):
    r1 = pow(10.0, p1_rating / 400.0)
    r2 = pow(10.0, p2_rating / 400.0)
    # print('r1 = %g, r2 = %g' % (r1, r2))

    e1 = r1 / (r1 + r2)
    e2 = r2 / (r1 + r2)
    # print('e1 = %g, e2 = %g' % (e1, e2))

    total = p1_score + p2_score
    s1 = p1_score / total
    s2 = p2_score / total
    # print('s1 = %g, s2 = %g' % (s1, s2))

    p1_change = K * (s1 - e1)
    p2_change = K * (s2 - e2)
    # print("r'1 = %g, r'2 = %g" % (r1, r2))

    return [p1_change, p2_change]
