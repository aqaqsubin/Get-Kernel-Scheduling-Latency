import os
import sys

REDIRECT_PATH = './parsing_result'
REPORT_FILE_PATH = './trace_report'
USEC_PER_SEC = 1000000

def irq_latency_report(file_path, irq_num):
    interval = 0
    markA = None
    markB = None

    sumOfLatency = 0
    minLatency = sys.float_info.max
    maxLatency = sys.float_info.min

    cycle_num = 0

    redirect_file_name = os.path.join(REDIRECT_PATH,file_path.split('/')[2])
    
    with open(redirect_file_name, 'w') as w:
        
        f = open(file_path, 'r')
        lines = f.readlines()
        f.close()

        del lines[0]

        for i, line in enumerate(lines):
            token = line.split(' ')
            token = ' '.join(token).split()
                        
            if token[3] == 'irq_handler_entry' and token[4] == "irq="+str(irq_num) : 

                markA = float(token[2].strip(":"))
                print("Marking A : {}".format(markA))

            elif token[3] == 'sched_switch:' and markA is not None \
                and token[token.index("==>")+1]== task +":"+ str(pid):
                
                markB = float(token[2].strip(":"))

                interval = (markB-markA) * USEC_PER_SEC 

                print("Marking B : {}".format(markB))
                print("{} cycle, Latency : {} usec \n".format(cycle_num, interval))
                w.write("{} cycle, Latency : {} usec \n".format(cycle_num+1, interval))
                
                cycle_num = cycle_num + 1
                
                if interval < minLatency : minLatency = interval
                if interval > maxLatency : maxLatency = interval
                sumOfLatency = sumOfLatency + interval
                
                markA = None
                markB = None
                interval = 0
        
        try : averageLatency = sumOfLatency/cycle_num
        except: averageLatency = 0            

        w.write("\nAverage Latency : {} usec \n".format(averageLatency))
        w.write("Max Latency : {} usec \n".format(maxLatency))
        w.write("Min Latency : {} usec \n".format(minLatency))




def wakeup_latency_report(file_path, task, pid):
    interval = 0
    markA = None
    markB = None

    sumOfLatency = 0
    minLatency = sys.float_info.max
    maxLatency = sys.float_info.min

    minLatency_timestamp = 0
    maxLatency_timestamp = 0

    cycle_num = 0

    redirect_file_name = os.path.join(REDIRECT_PATH,file_path.split('/')[2])
    
    with open(redirect_file_name, 'w') as w:
        
        f = open(file_path, 'r')
        lines = f.readlines()
        f.close()

        del lines[0]

        for i, line in enumerate(lines):

            token = line.split()
            token = ' '.join(token).split()
            
            if len(token) == 0 : break

            if token[3] == 'sched_wakeup:' and token[4] == task +":"+ str(pid) and token[6] == "success=1": 

                markA = float(token[2].strip(":"))

            elif token[3] == 'sched_switch:' and markA is not None \
                and token[token.index("==>")+1]== task +":"+ str(pid):
                
                markB = float(token[2].strip(":"))
                interval = (markB-markA) * USEC_PER_SEC 

                w.write("{} cycle, Latency : {} usec \n".format(cycle_num+1, interval))
                
                if interval < minLatency : 
                    minLatency = interval
                    minLatency_timestamp = float(token[2].strip(":"))
                if interval > maxLatency : 
                    maxLatency = interval
                    maxLatency_timestamp = float(token[2].strip(":"))
                    
                sumOfLatency = sumOfLatency + interval
                
                markA = None
                markB = None
                interval = 0
                
                cycle_num = cycle_num + 1
                
        try : averageLatency = sumOfLatency/cycle_num
        except: averageLatency = 0            

        w.write("\nAverage Latency : {} usec \n".format(averageLatency))
        w.write("Max Latency: {} usecs at timestamp: {} \n".format(maxLatency, maxLatency_timestamp))
        w.write("Min Latency: {} usecs at timestamp: {} \n".format(minLatency, minLatency_timestamp))

if __name__=='__main__':
    wakeup_latency_report(os.path.join(REPORT_FILE_PATH, "report_full_second_1555.txt"), "cyclictest", 4770)
    wakeup_latency_report(os.path.join(REPORT_FILE_PATH, "report_full_second_1556.txt"), "cyclictest", 4774)
    wakeup_latency_report(os.path.join(REPORT_FILE_PATH, "report_full_second_1557.txt"), "cyclictest", 4779)
    wakeup_latency_report(os.path.join(REPORT_FILE_PATH, "report_full_second_1558.txt"), "cyclictest", 4783)

