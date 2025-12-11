import TopArtistsCard from "./cards/TopArtistsCard";
import TopTitlesCard from "./cards/TopTitlesCard";
import TopGenresCard from "./cards/TopGenresCard";
import CountsCard from "./cards/CountsCard";
import DurationsCard from "./cards/DurationsCard";
import MonthlyChartCard from "./cards/MonthlyChartCard";

const cardClass = "bg-white rounded-2xl shadow-lg p-6 border border-gray-100";

function DashboardDisplay() {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-6 p-6">
      <TopTitlesCard cardClass={cardClass} />
      <TopArtistsCard cardClass={cardClass} />
      <TopGenresCard cardClass={cardClass} />
      <CountsCard cardClass={cardClass} />
      <DurationsCard cardClass={cardClass} />
      <MonthlyChartCard cardClass={cardClass} />
    </div>
  );
}

export default DashboardDisplay;
