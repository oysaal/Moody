// Data for 5 different moods
const happy = [5, 8, 7, 6, 9, 8, 9, 7, 6, 8, 7, 8, 6, 7, 8, 9, 8, 9, 7, 8, 7, 6, 8, 7, 9, 8, 7, 6, 9, 8];
const sad = [2, 3, 4, 2, 3, 2, 4, 5, 3, 2, 4, 5, 6, 5, 4, 3, 2, 3, 4, 5, 6, 5, 4, 2, 3, 2, 3, 4, 5, 4];
const angry = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2];
const excited = [4, 5, 6, 5, 4, 5, 6, 5, 4, 5, 6, 5, 4, 5, 6, 5, 4, 5, 6, 5, 4, 5, 6, 5, 4, 5, 6, 5, 4, 5];
const calm = [6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7, 6, 7];

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
