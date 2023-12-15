async function generateVideo() {
    const text = document.getElementById('text').value;
    const avatarType = document.getElementById('avatarType').value;

    try {
      const response = await fetch('http://localhost:3000/generateVideo', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, avatarType }),
      });

      const data = await response.json();
      alert(data.message);
    } catch (error) {
      console.error('Error:', error);
    }
}
