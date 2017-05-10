from ipykernel.kernelbase import Kernel

class EchoKernel(Kernel):
    implementation = 'Echo'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {'mimetype': 'text/plain'}
    banner = "Echo kernel - as useful as a parrot"

    def call_python(self, code):
        import subprocess

        with open("/Users/hamidbagheri/Documents/DS/MSR/program/test.boa","w") as f:
            f.write(code)

        bashCommand= 'java -jar ds.jar /Users/hamidbagheri/Documents/DS/MSR/program/test.boa  /Users/hamidbagheri/Documents/DS/MSR/data /Users/hamidbagheri/Documents/DS/MSR/output'

        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()



        if process.returncode !=0:
            return error

        with open("/Users/hamidbagheri/Documents/DS/MSR/output/part-r-00000","r") as f:
            content=f.read()

        #if process.returncode !=0:
        #    return error
        #else:
        return content

    def call_bash(self, code):
        import subprocess

        with open("/Users/hamidbagheri/Documents/DS/MSR/program/test.boa","w") as f:
            f.write(code)

        bashCommand= 'java -jar ds.jar /Users/hamidbagheri/Documents/DS/MSR/program/test.boa  /Users/hamidbagheri/Documents/DS/MSR/data /Users/hamidbagheri/Documents/DS/MSR/output'

        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()



        if process.returncode !=0:
            return error

        with open("/Users/hamidbagheri/Documents/DS/MSR/output/part-r-00000","r") as f:
            content=f.read()

        #if process.returncode !=0:
        #    return error
        #else:
        return content


    def call_boa(self, code):
        import subprocess

        with open("/Users/hamidbagheri/Documents/DS/MSR/program/test.boa","w") as f:
            f.write(code)


        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()



        if process.returncode !=0:
            return error

        with open("/Users/hamidbagheri/Documents/DS/MSR/output/part-r-00000","r") as f:
            content=f.read()

        #if process.returncode !=0:
        #    return error
        #else:
        return content



    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            strReturn=self.call_boa(code)
            stream_content = {'name': 'stdout', 'text': strReturn}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=EchoKernel)
