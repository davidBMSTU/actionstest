import sys

from cotea.runner import runner
from cotea.arguments_maker import argument_maker

pb_path = "cotea_run_files/main.yaml"
inv_path = "cotea_run_files/inv"

arg_maker = argument_maker()
arg_maker.add_arg("-i", inv_path)


r = runner(pb_path, arg_maker, show_progress_bar=True)

while r.has_next_play():
    while r.has_next_task():
        r.run_next_task()

r.finish_ansible()

if r.was_error():
    print("ansible-playbook launch - ERROR:")
    print(r.get_error_msg())

    sys.exit(1)
else:
    print("ansible-playbook launch - OK")
