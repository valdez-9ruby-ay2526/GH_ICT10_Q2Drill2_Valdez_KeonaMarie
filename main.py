# Monarch Dance Club Checker
from pyscript import document


def check_member(e):
    result = document.getElementById('result')

    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()

    dance_members = ['maria samantha', 'shiloh jakobe', 'juan miguel', 'gurleen kaur', 'chalanie lumbang']
    full_name = f'{first_name} {last_name}'.lower()

    if full_name in dance_members:
        result.innerText = f'Welcome, {first_name} {last_name}! You are a member of Dance Club. 🪩'
    else:
        result.innerText = f'Sorry, {first_name} {last_name} is not a member of Dance Club.'
