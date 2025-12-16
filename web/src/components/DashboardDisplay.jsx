import { useState, useEffect } from "react";

import { useStatistics } from "../context/StatisticsContext";

import ItemCard from "./cards/ItemCard";
import TopCard from "./cards/TopCard";
import NumberCard from "./cards/NumberCard";
import ChartCard from "./cards/ChartCard";

const visibleCard = "bg-base-100 rounded-2xl shadow-lg p-6 border border-base-200";
const invisibleCard = "rounded-2xl p-6";

function DashboardDisplay() {
  const { statistics, loading } = useStatistics();

  const [totalUniqueArtists, setTotalUniqueArtists] = useState(null);
  const [totalUniqueAlbums, setTotalUniqueAlbums] = useState(null);
  const [totalUniqueTitles, setTotalUniqueTitles] = useState(null);
  const [totalUniqueGenres, setTotalUniqueGenres] = useState(null);

  const [averageDailyCount, setAverageDailyCount] = useState(null);
  const [averageDailyDuration, setAverageDailyDuration] = useState(null);
  const [averageMonthlyCount, setAverageMonthlyCount] = useState(null);
  const [averageMonthlyDuration, setAverageMonthlyDuration] = useState(null);
  const [totalCount, setTotalCount] = useState(null);
  const [totalDuration, setTotalDuration] = useState(null);

  const [dataArtists, setDataArtists] = useState([]);
  const [dataAlbums, setDataAlbums] = useState([]);
  const [dataTitles, setDataTitles] = useState([]);
  const [dataGenres, setDataGenres] = useState([]);

  useEffect(() => {
    if (!statistics) return;

    setTotalUniqueArtists(statistics.summary?.items?.total_unique_artists ?? null);
    setTotalUniqueAlbums(statistics.summary?.items?.total_unique_albums ?? null);
    setTotalUniqueTitles(statistics.summary?.items?.total_unique_titles ?? null);
    setTotalUniqueGenres(statistics.summary?.items?.total_unique_genres ?? null);

    setAverageDailyCount(statistics.summary?.counts?.average_daily_count ?? null);
    setAverageDailyDuration(statistics.summary?.durations?.average_daily_duration ?? null);
    setAverageMonthlyCount(statistics.summary?.counts?.average_monthly_count ?? null);
    setAverageMonthlyDuration(statistics.summary?.durations?.average_monthly_duration ?? null);
    setTotalCount(statistics.summary?.counts?.total_count ?? null);
    setTotalDuration(statistics.summary?.durations?.total_duration ?? null);

    setDataArtists(
      Object.values(statistics.top?.artists ?? []).map((item) => ({
        primary: item.artist,
        secondary: `${item.duration.toLocaleString("fr-FR")} minutes`,
      }))
    );

    setDataAlbums(
      Object.values(statistics.top?.albums ?? []).map((item) => ({
        primary: `${item.album}`,
        secondary: `${item.artist} • ${item.duration.toLocaleString("fr-FR")} minutes`,
      }))
    );

    setDataTitles(
      Object.values(statistics.top?.titles ?? []).map((item) => ({
        primary: `${item.title}`,
        secondary: `${item.artist} • ${item.times.toLocaleString("fr-FR")} times`,
      }))
    );

    setDataGenres(
      Object.values(statistics.top?.genres ?? []).map((item) => ({
        primary: item.genre,
        secondary: `${item.duration.toLocaleString("fr-FR")} minutes`,
      }))
    );
  }, [statistics]);

  if (loading) return <div className={visibleCard}>Loading…</div>;

  return (
    <div className="bg-base-200 grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-5 p-5">
      <ItemCard cardClass={visibleCard} data={totalUniqueArtists} unit="artists" />
      <ItemCard cardClass={visibleCard} data={totalUniqueAlbums} unit="albums" />
      <ItemCard cardClass={visibleCard} data={totalUniqueTitles} unit="titles" />
      <ItemCard cardClass={visibleCard} data={totalUniqueGenres} unit="genres" />

      <TopCard cardClass={visibleCard} name="Top Artists" data={dataArtists} />
      <TopCard cardClass={visibleCard} name="Top Albums" data={dataAlbums} />
      <TopCard cardClass={visibleCard} name="Top Titles" data={dataTitles} />
      <TopCard cardClass={visibleCard} name="Top Genres" data={dataGenres} />

      <NumberCard cardClass={visibleCard} name="Daily Average" dataCount={averageDailyCount} dataDuration={averageDailyDuration} />
      <NumberCard cardClass={visibleCard} name="Monthly Average" dataCount={averageMonthlyCount} dataDuration={averageMonthlyDuration} />
      <NumberCard cardClass={visibleCard} name="Total" dataCount={totalCount} dataDuration={totalDuration} />
      <NumberCard cardClass={visibleCard} name="Undefined" dataCount={0} dataDuration={0} />

      <ChartCard cardClass={visibleCard} name="Chart" />
    </div>
  );
}

export default DashboardDisplay;
