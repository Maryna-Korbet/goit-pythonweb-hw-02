function checkHealth() {
  fetch('/healthchecker')
    .then((response) => {
      if (!response.ok) {
        return response.json().then((errorData) => {
          throw new Error(errorData.detail || 'Unknown error')
        })
      }
      return response.json()
    })
    .then((data) => {
      console.log(data)
      let responseDiv = document.getElementById('response')
      responseDiv.innerHTML = data.message
      responseDiv.className = 'response success'
    })
    .catch((error) => {
      let errorMessage = error.message
      if (errorMessage.startsWith('Error: ')) {
        errorMessage = errorMessage.substring(7)
      }
      document.getElementById('response').innerHTML =
        'Request error: ' + errorMessage
      document.getElementById('response').className = 'response error'
    })
}
