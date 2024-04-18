<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tagesplaner</title>
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }
  h1 {
    text-align: center;
  }
  #app {
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  form {
    display: flex;
    flex-direction: column;
  }
  input, button {
    margin-bottom: 10px;
    padding: 8px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }
  button {
    background-color: #007bff;
    color: white;
    cursor: pointer;
  }
  button:hover {
    background-color: #0056b3;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    margin-bottom: 10px;
  }
</style>
</head>
<body>
<h1>Tagesplaner</h1>
<div id="app">
</div>
<script>
const users = [
  { username: 'user1', password: 'password1' },
  { username: 'user2', password: 'password2' }
];

const tasks = [
  { title: 'Task 1', priority: 'High' },
  { title: 'Task 2', priority: 'Medium' },
  { title: 'Task 3', priority: 'Low' }
];

function authenticate(username, password) {
  return users.find(user => user.username === username && user.password === password);
}

function renderTasks(taskList) {
  const list = document.createElement('ul');
  taskList.forEach(task => {
    const listItem = document.createElement('li');
    listItem.textContent = ${task.title} - Priority: ${task.priority};
    list.appendChild(listItem);
  });
  return list;
}

function renderLoginForm(onSubmit) {
  const form = document.createElement('form');
  const usernameInput = document.createElement('input');
  const passwordInput = document.createElement('input');
  const submitButton = document.createElement('button');

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const username = usernameInput.value;
    const password = passwordInput.value;
    onSubmit(username, password);
  });

  usernameInput.placeholder = 'Username';
  passwordInput.placeholder = 'Password';
  passwordInput.type = 'password';
  submitButton.textContent = 'Login';

  form.appendChild(usernameInput);
  form.appendChild(passwordInput);
  form.appendChild(submitButton);

  return form;
}

function handleLogin(username, password) {
  const user = authenticate(username, password);
  if (user) {
    const appDiv = document.getElementById('app');
    appDiv.innerHTML = '';
    appDiv.appendChild(renderTasks(tasks));
  } else {
    alert('Invalid username or password');
  }
}

const appDiv = document.getElementById('app');
appDiv.appendChild(renderLoginForm(handleLogin));
</script>
</body>
</html>
