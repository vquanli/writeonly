#coding=utf8

import sim
import baidu

f_sim=sim.sim()
f_sim.sim_init('mkb3new.txt')
def writeonly(txt):
    ss= txt.encode("utf-8")
    baidu.q=ss
    tr=baidu.GetTrans()
    st=tr[(tr.find('dst')+6):(tr.find('"',tr.find('dst')+6))]
    result=f_sim.calc_sim(st)
    return result[1]
