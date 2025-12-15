import { useState, useEffect } from "react";

import { useStatistics } from "../context/StatisticsContext";

import TopCard from "./cards/TopCard";
import NumberCard from "./cards/NumberCard";
import ItemCard from "./cards/ItemCard";
import ChartCard from "./cards/ChartCard";

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

    setTotalUniqueArtists(statistics.summary.items.total_unique_artists);
    setTotalUniqueGenres(statistics.summary.items.total_unique_genres);
    setTotalUniqueTitles(statistics.summary.items.total_unique_titles);

    setAverageDailyCount(statistics.summary.counts.average_daily_count);
    setAverageMonthlyCount(statistics.summary.counts.average_monthly_count);
    setTotalCount(statistics.summary.counts.total_count);

    setAverageDailyDuration(statistics.summary.durations.average_daily_duration);
    setAverageMonthlyDuration(statistics.summary.durations.average_monthly_duration);
    setTotalDuration(statistics.summary.durations.total_duration);

    setDataArtists(
      Object.values(statistics.top.artists).map((item) => ({
        primary: item.artist,
        secondary: `${item.duration.toLocaleString("fr-FR")} minutes`,
      }))
    );

    setDataGenres(
      Object.values(statistics.top.genres).map((item) => ({
        primary: item.genre,
        secondary: `${item.duration.toLocaleString("fr-FR")} minutes`,
      }))
    );

    setDataTitles(
      Object.values(statistics.top.titles).map((item) => ({
        primary: `${item.title}`,
        secondary: `${item.artist} • ${item.times.toLocaleString("fr-FR")} times`,
      }))
    );
  }, [statistics]);

  if (loading) return <div className={visibleCard}>Loading…</div>;

  return (
    <div className="bg-base-200 grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-6 p-6">
      <ItemCard cardClass={visibleCard} data={totalUniqueArtists} unit="artists" />
      <ItemCard cardClass={visibleCard} data={totalUniqueGenres} unit="genres" />
      <ItemCard cardClass={visibleCard} data={totalUniqueTitles} unit="titles" />

      <TopCard cardClass={visibleCard} name="Top Artists" data={dataArtists} />
      <TopCard cardClass={visibleCard} name="Top Genres" data={dataGenres} />
      <TopCard cardClass={visibleCard} name="Top Titles" data={dataTitles} />

      <NumberCard cardClass={visibleCard} name="Daily Average" dataCount={averageDailyCount} dataDuration={averageDailyDuration} />
      <NumberCard cardClass={visibleCard} name="Monthly Average" dataCount={averageMonthlyCount} dataDuration={averageMonthlyDuration} />
      <NumberCard cardClass={visibleCard} name="Total" dataCount={totalCount} dataDuration={totalDuration} />

      <ChartCard cardClass={visibleCard} name="Chart" />
    </div>
  );
}

export default DashboardDisplay;
