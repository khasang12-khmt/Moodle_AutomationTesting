from concurrent.futures import ThreadPoolExecutor, wait
import time

class PerformanceRunner:
    def __init__(self, num_workers=1):
        self.__num_workers = num_workers
    
    def setWorker(self, workers):
        self.__num_workers = workers
        
    def run(self, task_class, num_workers, **kwargs):
        try:
            tasks = [task_class(**kwargs) for _ in range(num_workers)]
            with ThreadPoolExecutor(max_workers=num_workers) as executor:
                futures = [executor.submit(task.run_task) for task in tasks]
            wait(futures)
            success = 0
            failure = 0
            for idx, f in enumerate(futures):
                result = f.result()
                if isinstance(result, Exception):
                    print(f'Result {idx}: False, Error: {result=}')
                    failure += 1
                else:
                    print(f'Result {idx}: {result}, Error: None')
                    success += 1 if f.result() else 0
            print(f"""=======Run Succesfully with======== 
    Success: {success}, Failure: {failure}
    Error rate: {failure/(success+failure)}   
                """)
            return futures, success, failure
        except Exception as e:
            print(f"Exception in thread execution: {e}")

        """ Run Performance Task In Ram Up Pattern
            @param task_class: class of the task
            @param stable_count: number of run at max worker
            @param steps: number of incremental steps per ram up
        """
        
    def ramp_up_pattern(self, task_class, stable_count, step=1, **kwargs):
        try:
            print("Starting Ramp-Up Pattern...")
            ramp_up_workers = 1
            summary = [0,0]
            last_run = False
            count = 1
            while ramp_up_workers <= self.__num_workers:
                print(f"-- Run {count}-- Num workers: {ramp_up_workers}")
                count = count + 1
                _, success, failure = self.run(task_class, ramp_up_workers, **kwargs)
                summary[0], summary[1] = summary[0]+success, summary[1]+failure
                
                if last_run:
                    break
                if(ramp_up_workers + step > self.__num_workers):
                    ramp_up_workers = self.__num_workers
                    last_run = True
                else: 
                    ramp_up_workers = ramp_up_workers + step
                time.sleep(1)
            
            # Stable Run At Max Worker
            
            for i in range(1,stable_count+1):
                print(f"-- Run {count+i}-- Num workers: {self.__num_workers}")
                _, success, failure = self.run(task_class, self.__num_workers, **kwargs)
                summary[0], summary[1] = summary[0]+success, summary[1]+failure
                time.sleep(1)
                
            print(f"""   ========= Summary ==========
Success: {summary[0]}
Error: {summary[1]}
Error Rate: {summary[1] / (summary[0]+summary[1])}
                  """)

        except Exception as e:
            print(f"Exception in thread execution: {e}")
            

    def stable_pattern(self, task_class, stable_count, **kwargs):
        try:
            print("Starting Stable Pattern...")
            summary = [0,0]
            count = 1
            while count <= stable_count:
                print(f"-- Run {count}--")
                count = count + 1
                _, success, failure = self.run(task_class, self.__num_workers, **kwargs)
                summary[0], summary[1] = summary[0]+success, summary[1]+failure
                time.sleep(1)
            print(f"""   ========= Summary ==========
Success: {summary[0]}
Error: {summary[1]}
Error Rate: {summary[1] / (summary[0]+summary[1])}
                  """)
            return summary
        except Exception as e:
            print(f"Exception in thread execution: {e}")
