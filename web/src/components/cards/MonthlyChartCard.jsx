import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, LabelList } from "recharts";

import { useStatistics } from "../../context/StatisticsContext";

function MonthlyChartCard({ cardClass }) {
  const { statistics, loading } = useStatistics();

  if (loading) return <div className={cardClass}>Loading…</div>;
  if (!statistics) return <div className={cardClass}>No Data</div>;

  const { months } = statistics;

  const allMonths = [
    {number: "01", name: "January"},
    {number: "02", name: "February"},
    {number: "03", name: "March"},
    {number: "04", name: "April"},
    {number: "05", name: "May"},
    {number: "06", name: "June"},
    {number: "07", name: "July"},
    {number: "08", name: "August"},
    {number: "09", name: "September"},
    {number: "10", name: "October"},
    {number: "11", name: "November"},
    {number: "12", name: "December"},
  ];

  const data = allMonths.map((m) => {
    const info = months[m.number];

    return {
      month: m.name,
      artist: info ? info.artist : "",
      duration: info ? info.duration : 0,
      totalDuration: info ? info.total_duration : 0,
    };
  });

  return (
    <div className={`${cardClass} col-span-full`}>
      <h2 className="text-xl font-semibold mb-4">Monthly Chart (Duration)</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data} margin={{ top: 20, right: 20, left: 0, bottom: 20 }}>
          <XAxis dataKey="month" />
          <YAxis />
          <Tooltip
            formatter={(value, name, props) => {
              const artist = props.payload.artist;
              return [`${value} min`, `${artist}`];
            }}
            labelFormatter={(label) => `Month: ${label}`}
            contentStyle={{ fontSize: "14px" }}
          />
          <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
          <Bar dataKey="duration" fill="#4f46e5" barSize={50}>
            <LabelList 
              dataKey="artist" 
              position="top" 
              style={{ fontSize: 12, fill: "#333" }} 
            />
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default MonthlyChartCard;
