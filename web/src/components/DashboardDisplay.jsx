import { useState, useEffect } from "react";

import { useStatistics } from "../context/StatisticsContext";

import TopFiveCard from "./cards/TopFiveCard";
import NumberCard from "./cards/NumberCard";
import ItemCard from "./cards/ItemCard";
import MonthlyChartCard from "./cards/MonthlyChartCard";

const visibleCard = "bg-base-100 rounded-2xl shadow-lg p-6 border border-base-200";
const invisibleCard = "rounded-2xl p-6";

function DashboardDisplay() {
  const { statistics, loading } = useStatistics();

  const [totalUniqueArtists, setTotalUniqueArtists] = useState(0);
  const [totalUniqueGenres, setTotalUniqueGenres] = useState(0);
  const [totalUniqueTitles, setTotalUniqueTitles] = useState(0);

  const [averageDailyCount, setAverageDailyCount] = useState(0);
  const [averageMonthlyCount, setAverageMonthlyCount] = useState(0);
  const [totalCount, setTotalCount] = useState(0);

  const [averageDailyDuration, setAverageDailyDuration] = useState(0);
  const [averageMonthlyDuration, setAverageMonthlyDuration] = useState(0);
  const [totalDuration, setTotalDuration] = useState(0);

  const [dataArtists, setDataArtists] = useState([]);
  const [dataGenres, setDataGenres] = useState([]);
  const [dataTitles, setDataTitles] = useState([]);

  useEffect(() => {
    if (!statistics) return;

    setTotalUniqueArtists(statistics.counts.total_unique_artists);
    setTotalUniqueGenres(statistics.counts.total_unique_genres);
    setTotalUniqueTitles(statistics.counts.total_unique_titles);

    setAverageDailyCount(statistics.counts.average_daily_count);
    setAverageMonthlyCount(statistics.counts.average_monthly_count);
    setTotalCount(statistics.counts.total_count);

    setAverageDailyDuration(statistics.durations.average_daily_duration);
    setAverageMonthlyDuration(statistics.durations.average_monthly_duration);
    setTotalDuration(statistics.durations.total_duration);

    setDataArtists(
      Object.values(statistics.artists).map((item) => ({
        primary: item.artist,
        secondary: item.length,
      }))
    );

    setDataGenres(
      Object.values(statistics.genres).map((item) => ({
        primary: item.genre,
        secondary: item.length,
      }))
    );

    setDataTitles(
      Object.values(statistics.titles).map((item) => ({
        primary: `${item.artist} - ${item.title}`,
        secondary: item.times,
      }))
    );
  }, [statistics]);

  if (loading) return <div className={visibleCard}>Loading…</div>;

  return (
    <div className="bg-base-200 grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-6 p-6">
      <ItemCard cardClass={invisibleCard} data={totalUniqueArtists} unit="artists" />
      <ItemCard cardClass={invisibleCard} data={totalUniqueGenres} unit="genres" />
      <ItemCard cardClass={invisibleCard} data={totalUniqueTitles} unit="titles" />

      <NumberCard cardClass={visibleCard} name="Average Daily Count" data={averageDailyCount} unit="titles" />
      <NumberCard cardClass={visibleCard} name="Average Monthly Count" data={averageMonthlyCount} unit="titles" />
      <NumberCard cardClass={visibleCard} name="Total Count" data={totalCount} unit="titles" />

      <NumberCard cardClass={visibleCard} name="Average Daily Duration" data={averageDailyDuration} unit="minutes" />
      <NumberCard cardClass={visibleCard} name="Average Monthly Duration" data={averageMonthlyDuration} unit="minutes" />
      <NumberCard cardClass={visibleCard} name="Total Duration" data={totalDuration} unit="minutes" />

      <TopFiveCard cardClass={visibleCard} name="Top Artists" data={dataArtists} unit="minutes" />
      <TopFiveCard cardClass={visibleCard} name="Top Genres" data={dataGenres} unit="minutes" />
      <TopFiveCard cardClass={visibleCard} name="Top Titles" data={dataTitles} unit="times" />

      <MonthlyChartCard cardClass={visibleCard} />
    </div>
  );
}

export default DashboardDisplay;
