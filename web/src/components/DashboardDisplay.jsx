import { useState, useEffect } from "react";

import { useStatistics } from "../context/StatisticsContext";

import TopFiveCard from "./cards/TopFiveCard";
import CountsCard from "./cards/CountsCard";
import DurationsCard from "./cards/DurationsCard";
import MonthlyChartCard from "./cards/MonthlyChartCard";

const cardClass = "bg-white rounded-2xl shadow-lg p-6 border border-gray-100";

function DashboardDisplay() {
  const { statistics, loading } = useStatistics();

  const [dataArtists, setDataArtists] = useState([]);
  const [dataGenres, setDataGenres] = useState([]);
  const [dataTitles, setDataTitles] = useState([]);

  useEffect(() => {
    if (!statistics) return;

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
        primary: item.title,
        secondary: item.times,
      }))
    );
  }, [statistics]);

  if (loading) return <div className={cardClass}>Loading…</div>;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-6 p-6">
      <TopFiveCard cardClass={cardClass} name="Top Artists" data={dataArtists} unit="minutes" />
      <TopFiveCard cardClass={cardClass} name="Top Genres" data={dataGenres} unit="minutes" />
      <TopFiveCard cardClass={cardClass} name="Top Titles" data={dataTitles} unit="times" />

      <CountsCard cardClass={cardClass} />
      <DurationsCard cardClass={cardClass} />
      <MonthlyChartCard cardClass={cardClass} />
    </div>
  );
}

export default DashboardDisplay;
