document
  .getElementById('submit-button')
  .addEventListener('click', PostSummarize);
document.getElementById('post-url').addEventListener('click', PostURL);
document.getElementById('get-url').addEventListener('click', GetUrl);

document.getElementById('get-button').addEventListener('click', GetSummarize);

function PostSummarize() {
  const text = document.getElementById('text-to-summarize').value;
  document.getElementById('submit-button').innerHTML =
    'Getting Summary 😃!, Please Wait..';
  if (text !== '') {
    fetch('http://127.0.0.1:5000/', {
      method: 'POST',
      body: JSON.stringify(text),
      headers: new Headers({
        'content-type': 'application/json',
      }),
    })
      .then(() => {
        document.getElementById('submit-button').innerHTML = 'Submit Text!';
        document.getElementById('get-button').style.display = 'block';
      })
      .catch(() => (document.getElementById('error').style.display = 'block'));
    // console.log(text);
  }
}

function GetSummarize() {
  // const text = document.getElementById('text-to-summarize').value;

  fetch('http://127.0.0.1:5000/', {
    method: 'GET',
  })
    .then((res) => res.json())
    .then((res) => {
      text = res.text[res.text.length - 1];
      document.getElementById('after-summary').innerHTML = text[0];
      document.getElementById('readingTime').innerHTML = text[1];
      document.getElementById('entire-summary-div').style.display = 'block';
    })
    .catch(() => (document.getElementById('error').style.display = 'block'));
  // console.log(text);
}

function PostURL() {
  const url = document.getElementById('url').value;
  if (url !== '') {
    document.getElementById('post-url').innerHTML =
      'Getting Summary! 😃, Please Wait..';
    fetch('http://127.0.0.1:5000/texturl', {
      method: 'POST',
      body: JSON.stringify(url),
      headers: new Headers({
        'content-type': 'application/json',
      }),
    })
      .then(() => {
        document.getElementById('post-url').innerHTML = 'Submit URL!';
        document.getElementById('get-url').style.display = 'block';
      })
      .catch(() => (document.getElementById('error').style.display = 'block'));
    // console.log(text);
  }
}

function GetUrl() {
  // const text = document.getElementById('text-to-summarize').value;

  fetch('http://127.0.0.1:5000/texturl', {
    method: 'GET',
  })
    .then((res) => res.json())
    .then((res) => {
      text = res.urltext[res.urltext.length - 1];
      document.getElementById('after-summary').innerHTML = text[0];
      document.getElementById('readingTime').innerHTML = text[1];
      document.getElementById('entire-summary-div').style.display = 'block';
    })
    .catch(() => (document.getElementById('error').style.display = 'block'));
  // console.log(text);
}
