import time
import memory_profiler as mem_profile


def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
            'id': i,
            'name': 'name',
            'major': 'computer science'
        }
    return result


def people_generator(num_people):
    for i in xrange(num_people):
        person = {
            'id': i,
            'name': 'name',
            'major': 'computer science'
        }
        yield person


#t1 = time.perf_counter()
#people = people_list(10000000)
#t2 = time.perf_counter()

# Memory (After) : [15.4296875]Mb
# Tool 0.74476 Seconds

t1 = time.perf_counter()
people = people_generator(10000000)
t2 = time.perf_counter()

# Memory (After) : [15.4375]Mb
# Tool 5.000000000005e-07 Seconds

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage()))
print('Tool {} Seconds' .format(t2-t1))
