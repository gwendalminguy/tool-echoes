import { useState } from "react";

import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, LabelList } from "recharts";

import { useStatistics } from "../../context/StatisticsContext";

function MonthlyChartCard({ cardClass }) {
  const { statistics, loading } = useStatistics();
  const [key, setKey] = useState("topArtist");

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
      monthNumber: m.number,
      monthName: m.name,
      artist: info ? info.artist : "",
      duration: info ? info.duration : 0,
      totalCount: info ? info.total_count : 0,
      totalDuration: info ? info.total_duration : 0,
    };
  });

  return (
    <div className={`${cardClass} col-span-full`}>
      <div className="flex flex-row justify-between">
        {/* Title */}
        <h2 className="text-lg font-semibold mb-4">Monthly Chart</h2>

        {/* Tabs */}
        <div className="tabs tabs-box h-8">
          <input onClick={() => setKey("topArtist")} type="radio" name="monthly_chart_tabs" className="tab h-6" aria-label="Top Artist" defaultChecked />
          <input onClick={() => setKey("totalCount")} type="radio" name="monthly_chart_tabs" className="tab h-6" aria-label="Total Count" />
          <input onClick={() => setKey("totalDuration")} type="radio" name="monthly_chart_tabs" className="tab h-6" aria-label="Total Duration" />
        </div>
      </div>

      {/* Chart */}
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data} margin={{ top: 25, right: 5, left: 0, bottom: 20 }}>
          <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
          <XAxis dataKey="monthNumber" />
          <YAxis />
          <Tooltip
            formatter={(value) =>
              key === "totalCount"
                ? [`${value.toLocaleString("fr-FR")} titles`, "Count"]
                : [`${value.toLocaleString("fr-FR")} min`, "Duration"]
            }
            labelFormatter={(_, payload) => {
              if (!payload || !payload.length) return "";
              return payload[0].payload.monthName;
            }}
            contentStyle={{ fontSize: "14px", borderRadius: "10px" }}
          />
          <Bar dataKey={key === "topArtist" ? "duration" : key} fill="#4f46e5" barSize={50}>
            {key === "topArtist" && (
              <LabelList dataKey="artist" position="top" style={{ fontSize: 12, fill: "#333" }} />
            )}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default MonthlyChartCard;
