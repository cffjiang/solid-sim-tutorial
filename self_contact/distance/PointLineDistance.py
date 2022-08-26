import numpy as np

def val(p, e0, e1):
    e = e1 - e0
    numerator = e[1] * p[0] - e[0] * p[1] + e1[0] * e0[1] - e1[1] * e0[0]
    return numerator * numerator / np.dot(e, e)

def grad(p, e0, e1):
    g = np.array([0.0] * 6)
    t13 = -e1[0] + e0[0]
    t14 = -e1[1] + e0[1]
    t23 = 1.0 / (t13 * t13 + t14 * t14)
    t25 = ((e0[0] * e1[1] + -(e0[1] * e1[0])) + t14 * p[0]) + -(t13 * p[1])
    t24 = t23 * t23
    t26 = t25 * t25
    t27 = (e0[0] * 2.0 + -(e1[0] * 2.0)) * t24 * t26
    t26 *= (e0[1] * 2.0 + -(e1[1] * 2.0)) * t24
    g[0] = t14 * t23 * t25 * 2.0
    g[1] = t13 * t23 * t25 * -2.0
    t24 = t23 * t25
    g[2] = -t27 - t24 * (-e1[1] + p[1]) * 2.0
    g[3] = -t26 + t24 * (-e1[0] + p[0]) * 2.0
    g[4] = t27 + t24 * (p[1] - e0[1]) * 2.0
    g[5] = t26 - t24 * (p[0] - e0[0]) * 2.0
    return g

def hess(p, e0, e1):
    H = np.array([0.0] * 36)
    t15 = -e0[0] + p[0]
    t16 = -e0[1] + p[1]
    t17 = -e1[0] + p[0]
    t18 = -e1[1] + p[1]
    t19 = -e1[0] + e0[0]
    t20 = -e1[1] + e0[1]
    t21 = e0[0] * 2.0 + -(e1[0] * 2.0)
    t22 = e0[1] * 2.0 + -(e1[1] * 2.0)
    t23 = t19 * t19
    t24 = t20 * t20
    t31 = 1.0 / (t23 + t24)
    t34 = ((e0[0] * e1[1] + -(e0[1] * e1[0])) + t20 * p[0]) + -(t19 * p[1])
    t32 = t31 * t31
    t33 = t32 * t31
    t35 = t34 * t34
    t60 = t31 * t34 * 2.0
    t59 = -(t19 * t20 * t31 * 2.0)
    t62 = t32 * t35 * 2.0
    t64 = t21 * t21 * t33 * t35 * 2.0
    t65 = t22 * t22 * t33 * t35 * 2.0
    t68 = t15 * t21 * t32 * t34 * 2.0
    t71 = t16 * t22 * t32 * t34 * 2.0
    t72 = t17 * t21 * t32 * t34 * 2.0
    t75 = t18 * t22 * t32 * t34 * 2.0
    t76 = t19 * t21 * t32 * t34 * 2.0
    t77 = t20 * t21 * t32 * t34 * 2.0
    t78 = t19 * t22 * t32 * t34 * 2.0
    t79 = t20 * t22 * t32 * t34 * 2.0
    t90 = t21 * t22 * t33 * t35 * 2.0
    t92 = t16 * t20 * t31 * 2.0 + t77
    t94 = -(t17 * t19 * t31 * 2.0) + t78
    t96 = (t18 * t19 * t31 * 2.0 + -t60) + t76
    t99 = (-(t15 * t20 * t31 * 2.0) + -t60) + t79
    t93 = t15 * t19 * t31 * 2.0 + -t78
    t35 = -(t18 * t20 * t31 * 2.0) + -t77
    t97 = (t17 * t20 * t31 * 2.0 + t60) + -t79
    t98 = (-(t16 * t19 * t31 * 2.0) + t60) + -t76
    t100 = ((-(t15 * t16 * t31 * 2.0) + t71) + -t68) + t90
    t19 = ((-(t17 * t18 * t31 * 2.0) + t75) + -t72) + t90
    t102_tmp = t17 * t22 * t32 * t34
    t76 = t15 * t22 * t32 * t34
    t22 = (((-(t15 * t17 * t31 * 2.0) + t62) + -t65) + t76 * 2.0) + t102_tmp * 2.0
    t33 = t18 * t21 * t32 * t34
    t20 = t16 * t21 * t32 * t34
    t79 = (((-(t16 * t18 * t31 * 2.0) + t62) + -t64) + -(t20 * 2.0)) + -(t33 * 2.0)
    t77 = (((t15 * t18 * t31 * 2.0 + t60) + t68) + -t75) + -t90
    t78 = (((t16 * t17 * t31 * 2.0 + -t60) + t72) + -t71) + -t90
    H[0] = t24 * t31 * 2.0
    H[1] = t59
    H[2] = t35
    H[3] = t97
    H[4] = t92
    H[5] = t99
    H[6] = t59
    H[7] = t23 * t31 * 2.0
    H[8] = t96
    H[9] = t94
    H[10] = t98
    H[11] = t93
    H[12] = t35
    H[13] = t96
    t35 = -t62 + t64
    H[14] = (t35 + t18 * t18 * t31 * 2.0) + t33 * 4.0
    H[15] = t19
    H[16] = t79
    H[17] = t77
    H[18] = t97
    H[19] = t94
    H[20] = t19
    t33 = -t62 + t65
    H[21] = (t33 + t17 * t17 * t31 * 2.0) - t102_tmp * 4.0
    H[22] = t78
    H[23] = t22
    H[24] = t92
    H[25] = t98
    H[26] = t79
    H[27] = t78
    H[28] = (t35 + t16 * t16 * t31 * 2.0) + t20 * 4.0
    H[29] = t100
    H[30] = t99
    H[31] = t93
    H[32] = t77
    H[33] = t22
    H[34] = t100
    H[35] = (t33 + t15 * t15 * t31 * 2.0) - t76 * 4.0
    return np.reshape(H, (6, 6))