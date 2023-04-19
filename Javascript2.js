// Data for one mood per day
const moodData = [
  { day: 1, mood: 'happy', rating: 5 },
  { day: 2, mood: 'sad', rating: 2 },
  { day: 3, mood: 'angry', rating: 1 },
  { day: 4, mood: 'excited', rating: 4 },
  { day: 5, mood: 'calm', rating: 6 },
  { day: 6, mood: 'happy', rating: 8 },
  // Add more data for the remaining days...
];

// Create separate arrays for each mood
const happy = moodData.filter((entry) => entry.mood === 'happy').map((entry) => entry.rating);
const sad = moodData.filter((entry) => entry.mood === 'sad').map((entry) => entry.rating);
const angry = moodData.filter((entry) => entry.mood === 'angry').map((entry) => entry.rating);
const excited = moodData.filter((entry) => entry.mood === 'excited').map((entry) => entry.rating);
const calm = moodData.filter((entry) => entry.mood === 'calm').map((entry) => entry.rating);

// X-axis labels (30 days)
const days = Array.from({ length: 30 }, (_, i) => i + 1);

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
      text: 'Mood Ratings over 30 Days',
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
