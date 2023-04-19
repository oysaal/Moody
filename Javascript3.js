// Mood data for each day (randomly generated)
const moodData = Array.from({ length: 31 }, (_, i) => {
  const moodOptions = ['happy', 'sad', 'angry', 'excited', 'calm'];
  const randomMood = moodOptions[Math.floor(Math.random() * moodOptions.length)];
  return { day: i + 1, mood: randomMood, rating: Math.floor(Math.random() * 10) + 1 };
});

// Separate arrays for each mood
const happy = moodData.filter((entry) => entry.mood === 'happy').map((entry) => entry.rating);
const sad = moodData.filter((entry) => entry.mood === 'sad').map((entry) => entry.rating);
const angry = moodData.filter((entry) => entry.mood === 'angry').map((entry) => entry.rating);
const excited = moodData.filter((entry) => entry.mood === 'excited').map((entry) => entry.rating);
const calm = moodData.filter((entry) => entry.mood === 'calm').map((entry) => entry.rating);

// X-axis labels (31 days)
const days = Array.from({ length: 31 }, (_, i) => i + 1);

// Create a Chart.js chart
const ctx = document.getElementById('mood-chart').getContext('2d');
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: days,
    datasets: [
      { label: 'Happy', data: happy },
      { label: 'Sad', data: sad },
      { label: 'Angry', data: angry },
      { label: 'Excited', data: excited },
      { label: 'Calm', data: calm },
    ],
  },
  options: {
    title: {
      display: true,
      text: 'Mood Ratings over 31 Days',
    },
    scales: {
      xAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: 'Days',
          },
        },
      ],
      yAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: 'Mood Rating',
          },
        },
      ],
    },
  },
});
