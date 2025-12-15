import { useState, useMemo } from "react";

import { BarChart, Bar, ReferenceLine, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, LabelList } from "recharts";

import { useStatistics } from "../../context/StatisticsContext";

import MonthSelector from "../MonthSelector";

function ChartCard({ cardClass, name }) {
  const { statistics, loading } = useStatistics();

  const currentMonth = String(new Date().getMonth() + 1).padStart(2, "0");
  const [selectedMonth, setSelectedMonth] = useState(currentMonth);
  const [metric, setMetric] = useState("duration");
  const [view, setView] = useState("months");

  if (loading) return <div className={cardClass}>Loading…</div>;
  if (!statistics) return <div className={cardClass}>No Data</div>;

  const { summary, calendar } = statistics;
  const { months } = calendar;

  const allMonths = [
    { number: "01", name: "January" },
    { number: "02", name: "February" },
    { number: "03", name: "March" },
    { number: "04", name: "April" },
    { number: "05", name: "May" },
    { number: "06", name: "June" },
    { number: "07", name: "July" },
    { number: "08", name: "August" },
    { number: "09", name: "September" },
    { number: "10", name: "October" },
    { number: "11", name: "November" },
    { number: "12", name: "December" },
  ];

  const getDaysData = (monthNumber) => {
    const days = months?.[monthNumber]?.days ?? {};
    const month = allMonths.find(m => m.number === monthNumber)?.name;

    return Object.entries(days)
      .sort(([a], [b]) => Number(a) - Number(b))
      .map(([day, data]) => ({
        dayNumber: day,
        monthName: month,
        artist: data?.top_artist ?? "",
        duration: data?.duration ?? 0,
        totalCount: data?.total_count ?? 0,
        totalDuration: data?.total_duration ?? 0,
    }));
  };

  const dataDays = useMemo(
    () => getDaysData(selectedMonth),
    [months, selectedMonth]
  );

  const dataMonths = allMonths.map((m) => {
    const data = months?.[m.number]?.summary;

    return {
      monthNumber: m.number,
      monthName: m.name,
      artist: data?.top_artist ?? "",
      duration: data?.duration ?? 0,
      averageCount: data?.average_daily_count ?? 0,
      averageDuration: data?.average_daily_duration ?? 0,
      totalCount: data?.total_count ?? 0,
      totalDuration: data?.total_duration ?? 0,
    };
  });

  const dataYear = {
    averageCount: summary.counts.average_monthly_count,
    averageDuration : summary.durations.average_monthly_duration,
  };

  const data = view === "months"
    ? dataMonths
    : dataDays;

  return (
    <div className={`${cardClass} col-span-full`}>
      <div className="flex flex-row justify-between">
        {/* Title */}
        <h2 className="text-lg font-semibold mb-4">{name}</h2>

        {/* Chart Tabs */}
        <div className="tabs tabs-box h-8">
          <input onClick={() => setMetric("duration")} type="radio" name="chart_tabs" className="tab h-6" aria-label="Top Artist" defaultChecked />
          <input onClick={() => setMetric("totalCount")} type="radio" name="chart_tabs" className="tab h-6" aria-label="Total Count" />
          <input onClick={() => setMetric("totalDuration")} type="radio" name="chart_tabs" className="tab h-6" aria-label="Total Duration" />
        </div>
      </div>

      {/* Chart */}
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data} margin={{ top: 25, right: 5, left: 0, bottom: 20 }}>
          <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
          <XAxis dataKey={view === "months" ? "monthNumber" : "dayNumber"} />
          <YAxis width="auto" />
          <Tooltip
            formatter={(value) =>
              metric === "totalCount"
                ? [`${value.toLocaleString("fr-FR")} titles`, "Count"]
                : [`${value.toLocaleString("fr-FR")} min`, "Duration"]
            }
            labelFormatter={(_, payload) => {
              if (!payload || !payload.length) return "";
              return view === "months"
                ? payload[0].payload.monthName
                : `${payload[0].payload.monthName} ${payload[0].payload.dayNumber}`
            }}
            contentStyle={{ fontSize: "14px", borderRadius: "10px" }}
          />
          {metric !== "duration" && (
            <ReferenceLine strokeDasharray="5 5" zIndex={1000} stroke="#4f46e5" y={
              view === "months"
                ? metric === "totalCount"
                  ? dataYear.averageCount
                  : dataYear.averageDuration
                : metric === "totalCount"
                  ? dataMonths[Number(selectedMonth) - 1].averageCount
                  : dataMonths[Number(selectedMonth) - 1].averageDuration
            } />
          )}
          <Bar dataKey={metric} fill="#4f46e5" barSize={view === "months" ? 75 : 25} radius={view === "months" ? [5, 5, 0, 0] : [3, 3, 0, 0]}>
            {metric === "duration" && (
              <LabelList dataKey="artist" position="top" style={{ fontSize: view === "months" ? 12 : 8, fill: "#333" }} />
            )}
          </Bar>
        </BarChart>
      </ResponsiveContainer>

      {/* View Tabs */}
      <div className="tabs tabs-box h-8 mb-4">
        <input onClick={() => setView("months")} type="radio" name="view_tabs" className="tab h-6 w-1/2" aria-label="Months" defaultChecked />
        <input onClick={() => setView("days")} type="radio" name="view_tabs" className="tab h-6 w-1/2" aria-label="Days" />
      </div>

      {/* Months */}
      {view === "days" && (
        <MonthSelector allMonths={allMonths} selectedMonth={selectedMonth} setSelectedMonth={setSelectedMonth} />
      )}
    </div>
  );
}

export default ChartCard;
